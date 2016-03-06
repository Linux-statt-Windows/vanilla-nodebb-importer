#!/usr/bin/env python2.7
#
# Picture Converter
#
# Converts pictures from one server for vanilla forums 
# and uploads them to another server
#
# (c) 2016 Linux statt Windows


import re
import Queue
import colorama
import subprocess

from threading import Thread, Event
from colorama import Fore, Back, Style

DOWNLOAD_IP = ''
DOWNLOAD_USER = ''
DOWNLOAD_DIRECTORY = ''

UPLOAD_IP = ''
UPLOAD_USER = ''
UPLOAD_DIRECTORY = ''

TMP_DIR = ''

VERSION = '1.0.0'


###################
#   DOWNLOADER    #
###################

class Downloader(Thread):

    def __init__(self, directory, addr, user, tmp_dir, queue):
        Thread.__init__(self)
        self.stop_event = Event()
        self.directory = directory
        self.addr = addr
        self.user = user
        self.tmp_dir = tmp_dir
        self.queue = queue

    def __get_directory_listing(self):
        try:
            cmd = ['ssh', self.user + '@' + self.addr, 'ls ' + self.directory]
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            r = s.communicate()
        except Exception as e:
            log_err(str(e))
        return r

    def __retrieve_image(self, filename):
        try:
            cmd = ['scp', self.user + '@' + self.addr + ':' + self.directory + filename, self.tmp_dir + filename]
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            r = s.communicate()
        except Exception as e:
            log_err(str(e))
        return r

    def run(self):
        # retrieve file list
        files = self.__get_directory_listing()[0].decode('utf-8').split('\n')
        files.pop() # remove last empty item

        for f in files:
            self.__retrieve_image(f)
            log('Downloaded ' + f)
            self.queue.put(f)

        self.queue.put('\x90\x90\x90\x90')
        log('Closing download thread')
        self.stop_event.set()
        return


#################
#   CONVERTER   # 
#################

class Converter(Thread):

    def __init__(self, inp_queue, out_queue, tmp_dir):
        Thread.__init__(self)
        self.stop_event = Event()
        self.pq = inp_queue
        self.oq = out_queue
        self.tmp_dir = tmp_dir

    def __update_filename(self, name):
        return re.sub('(\.[a-zA-Z]*)$', '.jpg', name)

    def __convert_normal(self, filename):
        try:
            cmd = 'convert ' + self.tmp_dir + filename + ' -quality 75 -resize 250x135 -density 96x96 ' + self.tmp_dir + 'p' + self.__update_filename(filename)
            s = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            r = s.communicate()
        except Exception as e:
            log_err(str(e))
        return r
    
    def __convert_thumbnail(self, filename):
        try:
            cmd = 'convert ' + self.tmp_dir + filename + ' -quality 75 -resize 40x40! -density 96x96 ' + self.tmp_dir + 'n' + self.__update_filename(filename)
            s = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
            r = s.communicate()
        except Exception as e:
            log_err(str(e))
        return r

    def run(self):
        while not self.stop_event.is_set():
            # get downloaded pic from download thread
            pic = self.pq.get()

            # stop worker after last item
            if pic.encode('hex') == '\x90\x90\x90\x90'.encode('hex'):
                self.pq.task_done()
                self.oq.put('\x90\x90\x90\x90')
                log('Closing converter thread')
                self.stop_event.set()
                break

            # TODO: convert picture
            self.__convert_normal(pic)
            self.__convert_thumbnail(pic)
            self.pq.task_done()
            
            # return converted pic to upload thread
            pic = self.__update_filename(pic)
            self.oq.put(('n' + pic, 'p' + pic))
        return


####################
#      UPLOAD      #
####################

class Uploader(Thread):

    def __init__(self, directory, addr, user, tmp_dir, queue):
        Thread.__init__(self)
        self.stop_event = Event()
        self.directory = directory
        self.addr = addr
        self.user = user
        self.tmp_dir = tmp_dir
        self.queue = queue

    def __upload(self, filename):
        try:
            cmd = ['scp', self.tmp_dir + filename, self.user + '@' + self.addr + ':' + self.directory + filename]
            s = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            r = s.communicate()
        except Exception as e:
            log_err(str(e))
        return r

    def run(self):
        while not self.stop_event.is_set():
            # get converted picture
            pic = self.queue.get()

            # stop worker after last item
            # NOTE: When the upload thread should upload, pic is always a tuple. If pic is a string, the upload thread should shut down
            if isinstance(pic, str):
                log('Closing upload thread')
                self.queue.task_done()
                self.stop_event.set()
                break
           
            # upload picture and remove item from queue
            for p in pic:
                self.__upload(p)
            self.queue.task_done()
        return


#####################
#       UTILS       # 
#####################

def log(text):
    print(Fore.GREEN + '==> ' + Fore.WHITE + text)


def log_warn(text):
    print(Fore.YELLOW + '==> Warning: ' + Fore.WHITE + text)


def log_err(text):
    print(Fore.RED + '==> Error: ' + Fore.WHITE + text)


# NOTE: If you use this script as module, call this function!
def simple_convert(download_directory, download_ip, download_user, tmp_dir, upload_directory, upload_ip, upload_user):
    if not download_directory or not download_ip or not download_user or not tmp_dir or not upload_directory or not upload_ip or not upload_user:
        return False
    
    # Process- and Uploadqueue
    pq = Queue.Queue()
    uq = Queue.Queue()

    log('Starting downloader thread')
    down = Downloader(download_directory, download_ip, download_user, tmp_dir, pq)
    down.start()
    
    log('Starting processing thread')
    pro = Converter(pq, uq, tmp_dir)
    pro.start()

    log('Starting upload thread')
    up = Uploader(upload_directory, upload_ip, upload_user, tmp_dir, uq)
    up.start()

    return True


def main():
    log('Picture Converter for Vanilla Forums')
    log('Version: ' + VERSION + '\n')
   
    # Process- and Uploadqueue
    pq = Queue.Queue()
    uq = Queue.Queue()

    log('Starting downloader thread')
    down = Downloader(DOWNLOAD_DIRECTORY, DOWNLOAD_IP, DOWNLOAD_USER, TMP_DIR, pq)
    down.start()
    
    log('Starting processing thread')
    pro = Converter(pq, uq, TMP_DIR)
    pro.start()

    log('Starting upload thread')
    up = Uploader(UPLOAD_DIRECTORY, UPLOAD_IP, UPLOAD_USER, TMP_DIR, uq)
    up.start()
    pass


if __name__ == '__main__':
    main()

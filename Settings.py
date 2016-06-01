"""
Author:             Michael Rong
                    <miro@electronic.works>
                    www.electronic.works

Creation Date:      2016-04-03

Copyright:          (c) 2016 Linux statt Windows
                    https://linux-statt-windows.org
"""


import re
import ConfigParser
import sys


class Settings:
    """
    Validated and initialized data from settings.conf and provides some getter-methods.
    """


    __sharedState = {}

    def __init__(self):

        self.__dict__ = self.__sharedState

        self.__nodebbSSHHost       = None
        self.__nodebbSSHUsername   = None
        self.__nodebbSSHPassword   = None
        self.__nodebbPicPath       = None
        self.__redisSSHHost        = None
        self.__redisSSHUsername    = None
        self.__redisSSHPassword    = None
        self.__redisDBNumber       = None
        self.__redisDBPassword     = None
        self.__vanillaSSHHost      = None
        self.__vanillaSSHUsername  = None
        self.__vanillaSSHPassword  = None
        self.__vanillaPicPath      = None
        self.__mysqlSSHHost        = None
        self.__mysqlSSHUsername    = None
        self.__mysqlSSHPassword    = None
        self.__mysqlLocalUsername  = None
        self.__mysqlLocalPassword  = None
        self.__mysqlRemoteUsername = None
        self.__mysqlRemotePassword = None
        self.__mysqlDBName         = None




    def getNodebbSSHHost(self):
        """
        Returns the NodeBB SSH hostname.

        @return     __nodebbSSHHost <ip address as string>
        """

        return self.__nodebbSSHHost




    def getNodebbSSHUsername(self):
        """
        Returns the NodeBB SSH username.

        @return     __nodebbSSHUsername <string>
        """

        return self.__nodebbSSHUsername




    def getNodebbSSHPassword(self):
        """
        Returns the NodeBB SSH password.

        @retrun     __nodebbSSHPassword <string>
        """

        return self.__nodebbSSHPassword




    def getNodebbPicPath(self):
        """
        Returns the path where NodeBB stores pictures.

        @return     __nodebbPicPath <string>
        """

        return self.__nodebbPicPath




    def getRedisSSHHost(self):
        """
        Returns the Redis SSH hostname.

        @return     __redisSSHHost <ip address as string>
        """

        return self.__redisSSHHost




    def getRedisSSHUsername(self):
        """
        Returns the Redis SSH username.

        @return     __redisSSHUsername <string>
        """

        return self.__redisSSHUsername




    def getRedisSSHPassword(self):
        """
        Returns the Redis SSH password.

        @return     __redisSSHPassword <string>
        """

        return self.__redisSSHPassword




    def getRedisDBNumber(self):
        """
        Returns the Redis database number.

        @return     __redisDBNumber <string>
        """

        return self.__redisDBNumber




    def getRedisDBPassword(self):
        """
        Returns the Redis database password.

        @return     __redisDBPassword <string>
        """

        return self.__redisDBPassword




    def getVanillaSSHHost(self):
        """
        Returns the Vanilla SSH hostname.

        @return     __vanillaSSHHost <ip address as string>
        """

        return self.__vanillaSSHHost




    def getVanillaSSHUsername(self):
        """
        Returns the Vanilla SSH username.

        @return     __vanillaSSHUsername <string>
        """

        return self.__vanillaSSHUsername




    def getVanillaSSHPassword(self):
        """
        Returns the Vanilla SSH password.

        @return     __vanillaSSHPassword <string>
        """

        return self.__vanillaSSHPassword




    def getVanillaPicPath(self):
        """
        Returns the path where Vanilla stores pictures.

        @return     __vanillaPicPath <string>
        """

        return self.__vanillaPicPath




    def getMysqlSSHHost(self):
        """
        Returns the MySQL SSH hostname.

        @return     __mysqlSSHHost <ip address as string>
        """

        return self.__mysqlSSHHost




    def getMysqlSSHUsername(self):
        """
        Returns the MySQL SSH username.

        @return     __mysqlSSHUsername <string>
        """

        return self.__mysqlSSHUsername




    def getMysqlSSHPassword(self):
        """
        Returns the MySQL SSH password.

        @return     __mysqlSSHPassword <string>
        """

        return self.__mysqlSSHPassword




    def getMysqlLocalUsername(self):
        """
        Returns the MySQL database username of your local machine.

        @return     __mysqlLocalUsername <string>
        """

        return self.__mysqlLocalUsername




    def getMysqlLocalPassword(self):
        """
        Returns the MySQL database password of your local machine.

        @return     __mysqlLocalPassword <string>
        """

        return self.__mysqlLocalPassword




    def getMysqlRemoteUsername(self):
        """
        Returns the MySQL database username of your remote machine.

        @return     __mysqlRemoteUsername <string>
        """

        return self.__mysqlRemoteUsername




    def getMysqlRemotePassword(self):
        """
        Returns the MySQL database password of your remote machine.

        @return     __mysqlRemotePassword <string>
        """

        return self.__mysqlRemotePassword




    def getMysqlDBName(self):
        """
        Returns the MySQL database name.
        The local and remote database name must be the same.

        @return     __mysqlDBName <string>
        """

        return self.__mysqlDBName




    def __checkInput(self, var, checkType):
        """
        Checks the settings in 'settings.conf'.

        @param      var <string>
                    The setting parameter.

        @param      checkType <string>
                    The type of parameter. Allowed values are ip, user, password, path, db, database and port.

        @return     True or False <boolean>
                    True, if the paramater ist valid. Otherwise false.
        """

        if (checkType == 'ip'):
            return (True if ((var == 'localhost' or re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$").match(var))) else False)
        elif (checkType == 'user'):
            return (True if (len(var) <= 20 and re.compile("[A-Za-z]").match(var)) else False)
        elif (checkType == 'password'):
            return (True if (len(var) <= 128) else False)
        elif (checkType == 'path'):
            return (True if (re.compile("^/(.*)/$").match(var)) else False)
        elif (checkType == 'db'):
            return (True if (re.compile("^[0-9][0-9]?$|^100$").match(var)) else False)
        elif (checkType == 'database'):
            return (True if (len(var) <= 25 and re.compile("[A-Za-z]").match(var)) else False)
        elif (checkType == 'port'):
            return (True if (re.compile("^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$").match(var)) else False)
        else:
            return False




    def initSettings(self):
        """
        Reads and sets the setup parameters of settings.conf and invokes the validation function.
        Raises an exception if one of the parameters can not be validated.
        """

        try:
            config = ConfigParser.RawConfigParser()
            config.read('config/settings.conf')

            self.__nodebbSSHHost       = config.get('NodeBB', 'sshHost')
            self.__nodebbSSHUsername   = config.get('NodeBB', 'sshUsername')
            self.__nodebbSSHPassword   = config.get('NodeBB', 'sshPassword')
            self.__nodebbPicPath       = config.get('NodeBB', 'picPath')
            self.__redisSSHHost        = config.get('Redis', 'sshHost')
            self.__redisSSHUsername    = config.get('Redis', 'sshUsername')
            self.__redisSSHPassword    = config.get('Redis', 'sshPassword')
            self.__redisDBNumber       = config.get('Redis', 'dbNumber')
            self.__redisDBPassword     = config.get('Redis', 'dbPassword')
            self.__vanillaSSHHost      = config.get('Vanilla', 'sshHost')
            self.__vanillaSSHUsername  = config.get('Vanilla', 'sshUsername')
            self.__vanillaSSHPassword  = config.get('Vanilla', 'sshPassword')
            self.__vanillaPicPath      = config.get('Vanilla', 'picPath')
            self.__mysqlSSHHost        = config.get('MySQL', 'sshHost')
            self.__mysqlSSHUsername    = config.get('MySQL', 'sshUsername')
            self.__mysqlSSHPassword    = config.get('MySQL', 'sshPassword')
            self.__mysqlLocalUsername  = config.get('MySQL', 'localUsername')
            self.__mysqlLocalPassword  = config.get('MySQL', 'localPassword')
            self.__mysqlRemoteUsername = config.get('MySQL', 'remoteUsername')
            self.__mysqlRemotePassword = config.get('MySQL', 'remotePassword')
            self.__mysqlDBName         = config.get('MySQL', 'dbName')

            if (self.__checkInput(self.__nodebbSSHHost, 'ip') == False):
                print "\033[31m\nConfig Error !!!"
                print "The IP-Address of your NodeBB instance can not be validated."
                print "See section 'NodeBB' -> 'sshHost' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__nodebbSSHUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH username of your NodeBB instance can not be validated."
                print "See section 'NodeBB' -> 'sshUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__nodebbSSHPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH password of your NodeBB instance can not be validated."
                print "See section 'NodeBB' -> 'sshPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__nodebbPicPath, 'path') == False):
                print "\033[31m\nConfig Error !!!"
                print "The picture path of your NodeBB instance can not be validated."
                print "See section 'NodeBB' -> 'picPath' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__redisSSHHost, 'ip') == False):
                print "\033[31m\nConfig Error !!!"
                print "The IP-Address of your Redis instance can not be validated."
                print "See section 'Redis' -> 'sshHost' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__redisSSHUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH username of your Redis instance can not be validated."
                print "See section 'Redis' -> 'sshUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__redisSSHPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH password of your Redis instance can not be validated."
                print "See section 'Redis' -> 'sshPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__redisDBNumber, 'db') == False):
                print "\033[31m\nConfig Error !!!"
                print "The database number of your Redis database can not be validated."
                print "See section 'Redis' -> 'dbNumber' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__redisDBPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The password of your Redis database can not be validated."
                print "See section 'Redis' -> 'dbPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__vanillaSSHHost, 'ip') == False):
                print "\033[31m\nConfig Error !!!"
                print "The IP-Address of your Vanilla instance can not be validated."
                print "See section 'Vanilla' -> 'sshHost' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__vanillaSSHUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH username of your Vanilla instance can not be validated."
                print "See section 'Vanilla' -> 'sshUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__vanillaSSHPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH password of your Vanilla instance can not be validated."
                print "See section 'Vanilla' -> 'sshPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__vanillaPicPath, 'path') == False):
                print "\033[31m\nConfig Error !!!"
                print "The picture path of your Vanilla instance can not be validated."
                print "See section 'Vanilla' -> 'picPath' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlSSHHost, 'ip') == False):
                print "\033[31m\nConfig Error !!!"
                print "The IP-Address of your MySQL instance can not be validated."
                print "See section 'MySQL' -> 'sshHost' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlSSHUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH username of your MySQL instance can not be validated."
                print "See section 'MySQL' -> 'sshUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlSSHPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The SSH password of your MySQL instance can not be validated."
                print "See section 'MySQL' -> 'sshPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlLocalUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The username of your local MySQL instance can not be validated."
                print "See section 'MySQL' -> 'localUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlLocalPassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The password of your local MySQL instance can not be validated."
                print "See section 'MySQL' -> 'localPassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlRemoteUsername, 'user') == False):
                print "\033[31m\nConfig Error !!!"
                print "The username of your remote MySQL instance can not be validated."
                print "See section 'MySQL' -> 'remoteUsername' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlRemotePassword, 'password') == False):
                print "\033[31m\nConfig Error !!!"
                print "The password of your remote MySQL instance can not be validated."
                print "See section 'MySQL' -> 'remotePassword' in /config/settings.conf.\033[0m\n"
                sys.exit(1)
            if (self.__checkInput(self.__mysqlDBName, 'database') == False):
                print "\033[31m\nConfig Error !!!"
                print "The database name of your MySQL database can not be validated."
                print "See section 'MySQL' -> 'dbName' in /config/settings.conf.\033[0m\n"
                sys.exit(1)

        except ConfigParser.NoSectionError:
            print "\033[31m\nConfig Error !!!"
            print "Can't find the config file.\033[0m\n"
            sys.exit(1)

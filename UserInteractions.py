"""
Author:             Michael Rong
                    <miro@electronic.works>
                    www.electronic.works

Creation Date:      2016-04-06

Copyright:          (c) 2016 Linux statt Windows
                    https://linux-statt-windows.org
"""


from Settings import *
import os
import sys


settings = Settings()


class UserInteractions:
    """
    Runs the dialog with the user and initializes the class 'Settings'
    """


    def __init__(self):

        self.__vanillaIsSameLikeNodebb    = False
        self.__nodebbIsSameLikeRedis      = False
        self.__vanillaIsSameLikeMysql     = False




    def __evaluation(self, screen):
        """
        Private method to respond to user input.

        @param      screen <string>
                    The screen of the user interaction.
        """

        while (True):
            answer = str(raw_input("-> "))

            if (answer == 'quit'):
                sys.exit(0)

            # First question
            elif (screen == 'screen01'):
                if (answer == 'yes'):
                    break
                elif (answer == 'no'):
                    sys.exit(0)
                elif (answer == 'help'):
                    self.__help('screen01')
                else:
                    self.__error('screen01')

            # NodeBB IP
            elif (screen == 'screen02'):
                if (answer == 'help'):
                    self.__help('screen02')
                elif (settings.setNodebbIP(answer)):
                    break
                else:
                    self.__error('screen02')

            # NodeBB SSH user
            elif (screen == 'screen03'):
                if (answer == 'help'):
                    self.__help('screen03')
                elif (settings.setNodebbUser(answer)):
                    break
                else:
                    self.__error('screen03')

            # NodeBB SSH password
            elif (screen == 'screen04'):
                if (answer == 'help'):
                    self.__help('screen04')
                elif (settings.setNodebbPassword(answer)):
                    break
                else:
                    self.__error('screen04')

            # NodeBB pic directory
            elif (screen == 'screen05'):
                if (answer == 'help'):
                    self.__help('screen05')
                elif (settings.setNodebbPicPath(answer)):
                    break
                else:
                    self.__error('screen05')

            # Vanilla IP
            elif (screen == 'screen06'):
                if (answer == 'help'):
                    self.__help('screen06')
                elif (answer == 'same'):
                    self.__vanillaIsSameLikeNodebb = True
                    settings.setVanillaIP(settings.getNodebbIP())
                    settings.setVanillaUser(settings.getNodebbUser())
                    settings.setVanillaPassword(settings.getNodebbPassword())
                    break
                elif (settings.setVanillaIP(answer)):
                    break
                else:
                    self.__error('screen06')

            # Vanilla SSH user
            elif (screen == 'screen07'):
                if (answer == 'help'):
                    self.__help('screen07')
                elif (settings.setVanillaUser(answer)):
                    break
                else:
                    self.__error('screen07')

            # Vanilla SSH password
            elif (screen == 'screen08'):
                if (answer == 'help'):
                    self.__help('screen08')
                elif (settings.setVanillaPassword(answer)):
                    break
                else:
                    self.__error('screen08')

            # Vanilla pic directory
            elif (screen == 'screen09'):
                if (answer == 'help'):
                    self.__help('screen09')
                elif (settings.setVanillaPicPath(answer)):
                    break
                else:
                    self.__error('screen09')

            # Redis IP
            elif (screen == 'screen10'):
                if (answer == 'help'):
                    self.__help('screen10')
                elif (answer == 'same'):
                    self.__nodebbIsSameLikeRedis = True
                    settings.setRedisIP(settings.getNodebbIP())
                    settings.setRedisUser(settings.getNodebbUser())
                    settings.setRedisPassword(settings.getNodebbPassword())
                    break
                elif (settings.setRedisIP(answer)):
                    break
                else:
                    self.__error('screen10')

            # Redis SSH user
            elif (screen == 'screen11'):
                if (answer == 'help'):
                    self.__help('screen11')
                elif (settings.setRedisUser(answer)):
                    break
                else:
                    self.__error('screen11')

            # Redis SSH password
            elif (screen == 'screen12'):
                if (answer == 'help'):
                    self.__help('screen12')
                elif (settings.setRedisPassword(answer)):
                    break
                else:
                    self.__error('screen12')

            # Redis port
            elif (screen == 'screen13'):
                if (answer == 'help'):
                    self.__help('screen13')
                elif (settings.setRedisPort(answer)):
                    break
                else:
                    self.__error('screen13')

            # Redis DB number
            elif (screen == 'screen14'):
                if (answer == 'help'):
                    self.__help('screen14')
                elif (settings.setRedisDB(answer)):
                    break
                else:
                    self.__error('screen14')

            # Redis DB password
            elif (screen == 'screen15'):
                if (answer == 'help'):
                    self.__help('screen15')
                elif (settings.setRedisDbPassword(answer)):
                    break
                else:
                    self.__error('screen15')

            # MySQL IP
            elif (screen == 'screen16'):
                if (answer == 'help'):
                    self.__help('screen16')
                elif (answer == 'same'):
                    self.__vanillaIsSameLikeMysql = True
                    settings.setMySqlIP(settings.getVanillaIP())
                    settings.setMySqlUser(settings.getVanillaUser())
                    settings.setMySqlPassword(settings.getVanillaPassword())
                    break
                elif (settings.setMySqlIP(answer)):
                    break
                else:
                    self.__error('screen16')

            # MySQL SSH user
            elif (screen == 'screen17'):
                if (answer == 'help'):
                    self.__help('screen17')
                elif (settings.setMySqlUser(answer)):
                    break
                else:
                    self.__error('screen17')

            # MySQL SSH password
            elif (screen == 'screen18'):
                if (answer == 'help'):
                    self.__help('screen18')
                elif (settings.setMySqlPassword(answer)):
                    break
                else:
                    self.__error('screen18')

            # MySQL port
            elif (screen == 'screen19'):
                if (answer == 'help'):
                    self.__help('screen19')
                elif (settings.setMySqlPort(answer)):
                    break
                else:
                    self.__error('screen19')

            # MySQL database name
            elif (screen == 'screen20'):
                if (answer == 'help'):
                    self.__help('screen20')
                elif (settings.setMySqlDbName(answer)):
                    break
                else:
                    self.__error('screen20')

            # MSQL database user
            elif (screen == 'screen21'):
                if (answer == 'help'):
                    self.__help('screen21')
                elif (settings.setMySqlDbUser(answer)):
                    break
                else:
                    self.__error('screen21')

            # MySQL database password
            elif (screen == 'screen22'):
                if (answer == 'help'):
                    self.__help('screen22')
                elif (settings.setMySqlDbPassword(answer)):
                    break
                else:
                    self.__error('screen22')

            else:
                self.__error('error')




    def __help(self, screen):
        """
        Private method to show help messages.

        @param      screen <string>
                    The screen of the user interaction.
        """

        # First question
        if (screen == 'screen01'):
            print("Type \033[1m'yes'\033[21m, if you have done the above step or \033[1m'no'\033[21m to quit!\n")
        # NodeBB IP
        elif (screen == 'screen02'):
            print("Please enter a valid \033[1mIP4-Address\033[21m. If NodeBB is a local instance type \033[1m'localhost'\033[21m!")
            print("The information is required to connect your NodeBB machine via SSH.\n")
        # NodeBB SSH user
        elif (screen == 'screen03'):
            print("Please enter the \033[1mSSH user name\033[21m of your NodeBB machine!")
            print("The information is required to connect your NodeBB machine via SSH.\n")
        # NodeBB SSH password
        elif (screen == 'screen04'):
            print("Please enter the \033[1mSSH password\033[21m of your NodeBB machine!")
            print("The information is required to connect your NodeBB machine via SSH.")
            print("This converter version supports only authentification via password.\n")
        # NodeBB pic directory
        elif (screen == 'screen05'):
            print("Please enter the \033[1mpath to the NodeBB profile pictures directory\033[21m!")
            print("The Information is required to download the profile pictures from your NodeBB machine.")
            print("Often you can find the pictures under \033[1m'.../nodebb/public/uploads/profile/'\033[21m")
            print("The path must begin and end with '/'.\n")
        # Vanilla IP
        elif (screen == 'screen06'):
            print("Please enter a valid \033[1mIP4-Address\033[21m! If Vanilla is a local instance type \033[1m'localhost'\033[21m!")
            print("If Vanilla resides on the same machine as NodeBB type \033[1m'same'\033[21m!")
            print("The information is required to connect your Vanilla machine via SSH.\n")
        # Vanilla SSH user
        elif (screen == 'screen07'):
            print("Please enter the \033[1mSSH user name\033[21m of your Vanilla machine!")
            print("The information is required to connect your Vanilla machine via SSH.\n")
        # Vanilla SSH password
        elif (screen == 'screen08'):
            print("Please enter the \033[1mSSH password\033[21m of your Vanilla machine!")
            print("The information is required to connect your Vanilla machine via SSH.")
            print("This converter version supports only authentification via password.\n")
        # Vanilla pic directory
        elif (screen == 'screen09'):
            print("Please enter the \033[1mpath to the Vanilla profile pictures directory\033[21m!")
            print("The Information is required to upload the profile pictures to your Vanilla machine.")
            print("Often you can find the pictures under \033[1m'.../vanilla/uploads/userpics/'\033[21m")
            print("The path must begin and end with '/'.\n")
        # Redis IP
        elif (screen == 'screen10'):
            print("Please enter a valid \033[1mIP4-Address\033[21m! If Redis is a local instance type \033[1m'localhost'\033[21m!")
            print("If Redis resides on the same machine as NodeBB type \033[1m'same'\033[21m!")
            print("The information is required to connect your Redis machine via SSH.\n")
        # Redis SSH user
        elif (screen == 'screen11'):
            print("Please enter the \033[1mSSH user name\033[21m of your Redis machine!")
            print("The information is required to connect your Redis machine via SSH.\n")
        # Redis SSH password
        elif (screen == 'screen12'):
            print("Please enter the \033[1mSSH password\033[21m of your Redis machine!")
            print("The information is required to connect your Redis machine via SSH.")
            print("This converter version supports only authentification via password.\n")
        # Redis port
        elif (screen == 'screen13'):
            print("Please enter the \033[1mport number\033[21m of your Redis machine!")
            print("The information is required to connect your Redis database.\n")
        # Redis DB number
        elif (screen == 'screen14'):
            print("Please enter the \033[1mdatabase nummber\033[21m of your Redis database!")
            print("The information is required to select the correct Redis database.")
            print("Often its just '0'\n")
        # Redis DB password
        elif (screen == 'screen15'):
            print("Please enter the Redis \033[1mdatabase password\033[21m!")
            print("Just press \033[1m'enter'\033[21m without further input, if no password exists.")
            print("The information ist required to access the Redis database.\n")
        # MySQL IP
        elif (screen == 'screen16'):
            print("Please enter a valid \033[1mIP4-Address\033[21m! If MySQL is a local instance type \033[1m'localhost'\033[21m!")
            print("If MySQL resides on the same machine as Vanilla type \033[1m'same'\033[21m")
            print("The information is required to connect your MySQL machine via SSH.\n")
        # MySQL SSH user
        elif (screen == 'screen17'):
            print("Please enter the \033[1mSSH user name\The screen of the user interaction.
        elif (screen == 'screen18'):
            print("Please enter the \033[1mSSH password\033[21m of your MySQL machine!")
            print("The information is required to connect your MySQL machine via SSH.")
            print("This converter version supports only authentification via password.\n")
        # MySQL port
        elif (screen == 'screen19'):
            print("Please enter the \033[1mport number\033[21m of your MySQL machine!")
            print("The information is required to connect your MySQL database.\n")
        # MySQL DB name
        elif (screen == 'screen20'):
            print("Please enter the \033[1mdatabase name\033[21m of your MySQL database!")
            print("It must be the same database name that you created during the Vanilla installation.")
            print("The information is required to select the correct MySQL database.")
            print("\033[1mATTENTION: All your old Vanilla data will be overwritten !!!\033[21m\n")
        # MySQL DB user
        elif (screen == 'screen21'):
            print("Please enter the MySQL \033[1muser name\033[21m!")
            print("The information is required to connect the MySQL server on your MySQL machine.\n")
        # MySQL DB password
        elif (screen == 'screen22'):
            print("Please enter the MySQL \033[1mpassword\033[21m!")
            print("The information is required to connect the MySQL server on your MySQL machine.\n")
        else:
            self.__error('error')




    def __error(self, screen):
        """
        Private method to show error messages.

        @param      screen <string>
                    The screen of the user interaction.
        """

        # First question
        if (screen == 'screen01'):
            print("\033[31mType \033[1m'yes'\033[21m, if you have done the above step or \033[1m'no'\033[21m to quit!\033[0m\n")
        # NodeBB IP
        elif (screen == 'screen02'):
            print("\033[31mPlease enter a valid IP4-Address!\nIf NodeBB is a local instance type 'localhost'!\033[0m\n")
        # NodeBB SSH user
        elif (screen == 'screen03'):
            print("\033[31mPlease enter the SSH user name of your NodeBB machine!\033[0m\n")
        # NodeBB SSH password
        elif (screen == 'screen04'):
            print("\033[31mPlease enter the SSH password of your NodeBB machine!\033[0m\n")
        # NodeBB pic directory
        elif (screen == 'screen05'):
            print("\033[31mPlease enter the path to the NodeBB profile pictures directory!\033[0m\n")
        # Vanilla IP
        elif (screen == 'screen06'):
            print("\033[31mPlease enter a valid IP4-Address!\nIf Vanilla is a local instance type 'localhost'!\nIf Vanilla resides on the same machine as NodeBB type 'same'\033[0m\n")
        # Vanilla SSH user
        elif (screen == 'screen07'):
            print("\033[31mPlease enter the SSH user name of your Vanilla machine!\033[0m\n")
        # Vanilla SSH password
        elif (screen == 'screen08'):
            print("\033[31mPlease enter the SSH password of your Vanilla machine!\033[0m\n")
        # Vanilla pic directory
        elif (screen == 'screen09'):
            print("\033[31mPlease enter the path to the Vanilla profile pictures directory!\033[0m\n")
        # Redis IP
        elif (screen == 'screen10'):
            print("\033[31mPlease enter a valid IP4-Address!\nIf Redis is a local instance type 'localhost'!\nIf Redis resides on the same machine as NodeBB type 'same'\033[0m\n")
        # Redis SSH user
        elif (screen == 'screen11'):
            print("\033[31mPlease enter the SSH user name of your Redis machine!\033[0m\n")
        # Redis SSH password
        elif (screen == 'screen12'):
            print("\033[31mPlease enter the SSH password of your Redis machine!\033[0m\n")
        # Redis port
        elif (screen == 'screen13'):
            print("\033[31mPlease enter the port number of your Redis machine!\033[0m\n")
        # Redis DB number
        elif (screen == 'screen14'):
            print("\033[31mPlease enter the database nummber of your Redis database!\033[0m\n")
        # Redis DB password
        elif (screen == 'screen15'):
            print("\033[31mPlease enter the password of your Redis database!\033[0m\n")
        # MySQL IP
        elif (screen == 'screen16'):
            print("\033[31mPlease enter a valid IP4-Address!\nIf MySQL is a local instance type 'localhost'!\nIf MySQL resides on the same machine as Vanilla type 'same'\033[0m\n")
        # MySQL SSH user
        elif (screen == 'screen17'):
            print("\033[31mPlease enter the SSH user name of your MySQL machine!\033[0m\n")
        # MySQL SSH password
        elif (screen == 'screen18'):
            print("\033[31mPlease enter the SSH password of your MySQL machine!\033[0m\n")
        # MySQL port
        elif (screen == 'screen19'):
            print("\033[31mPlease enter the port number of your MySQL machine!\033[0m\n")
        # MySQL DB name
        elif (screen == 'screen20'):
            print("\033[31mPlease enter the database name of your MySQL database!\033[0m\n")
        # MySQL DB user
        elif (screen == 'screen21'):
            print("\033[31mPlease enter the MySQL user name!\033[0m\n")
        # MySQL DB password
        elif (screen == 'screen22'):
            print("\033[31mPlease enter the MySQL password!\033[0m\n")

        else:
            print("\033[1;4;31m\nOops, something is going wrong!!!\033[0m")
            print("\033[31mThere is an internal error.")
            print("Please start the script again or create an error report.\033[0m\n\n")
            sys.exit(0)




    def __header(self):
        """
        Private method to show the header of the user dialog.
        """

        os.system("clear")
        print("\033[1;4m\nVanilla-NodeBB Importer\033[0m\n")
        print("Converted your NodeBB-Redis-Forum to Vanilla.")
        print("Type \033[1m'help'\033[21m to get some more informations or \033[1m'quit'\033[21m to escape.\n\n")




    def __screen01(self):
        """
        Private method to show the startup user dialog.
        """

        self.__header()
        print("The first step is that you install your Vanilla-Forum.")
        print("\033[31mATTENTION: All your old Vanilla data will be overwritten during converting !!!\033[0m\n")
        print("Type \033[1m'yes'\033[21m, if you have done this step or \033[1m'no'\033[21m to quit!\n")
        self.__evaluation('screen01')




    def __screen02(self):
        """
        Message to get the NodeBB IP-Address.
        """

        self.__header()
        print("Enter the IP4-Address (or 'localhost') of your NodeBB machine!\n")
        self.__evaluation('screen02')




    def __screen03(self):
        """
        Message to get the NodeBB SSH user name.
        """

        self.__header()
        print("Enter the SSH user name of your NodeBB machine!\n")
        self.__evaluation('screen03')




    def __screen04(self):
        """
        Message to get the NodeBB SSH password.
        """

        self.__header()
        print("Enter the SSH password of your NodeBB machine!\n")
        self.__evaluation('screen04')




    def __screen05(self):
        """
        Message to get the NodeBB path to the profile pictures directory.
        """

        self.__header()
        print("Enter the NodeBB path to your profile pictures directory!\n")
        self.__evaluation('screen05')




    def __screen06(self):
        """
        Message to get the Vanille IP-Address.
        """

        self.__header()
        print("Enter the IP4-Address (or 'localhost') of your Vanilla machine!")
        print("If its the same like NodeBB just type 'same'.\n")
        self.__evaluation('screen06')




    def __screen07(self):
        """
        Message to get the Vanilla SSH user name.
        """

        self.__header()
        print("Enter ths SSH user name of your Vanilla machine!\n")
        self.__evaluation('screen07')




    def __screen08(self):
        """
        Message to get the Vanilla SSH password.
        """

        self.__header()
        print("Enter the SSH password of your Vanilla machine!\n")
        self.__evaluation('screen08')




    def __screen09(self):
        """
        Message to get the Vanilla path to the profile pictures directory.
        """

        self.__header()
        print("Enter the Vanilla path to your profile pictures directory!\n")
        self.__evaluation('screen09')




    def __screen10(self):
        """
        Message to get the Redis IP-Address.
        """

        self.__header()
        print("Enter the IP4-Address (or 'localhost') of your Redis machine!")
        print("If its the same like NodeBB just type 'same'.\n")
        self.__evaluation('screen10')




    def __screen11(self):
        """
        Message to get the Redis SSH user name.
        """

        self.__header()
        print("Enter the SSH user name of your Redis machine!\n")
        self.__evaluation('screen11')




    def __screen12(self):
        """
        Message to get the Redis SSH password.
        """

        self.__header()
        print("Enter the SSH password of your Redis machine!\n")
        self.__evaluation('screen12')




    def __screen13(self):
        """
        Message to get the Redis port number.
        """

        self.__header()
        print("Enter the port number of your Redis machine!\n")
        self.__evaluation('screen13')




    def __screen14(self):
        """
        Message to get the Redis database number.
        """

        self.__header()
        print("Enter the database number of your Redis database!\n")
        self.__evaluation('screen14')




    def __screen15(self):
        """
        Message to get the Redis database password.
        """

        self.__header()
        print("Enter the password of your Redis database!\n")
        self.__evaluation('screen15')




    def __screen16(self):
        """
        Message to get the MySQL IP-Address.
        """

        self.__header()
        print("Enter the IP4-Address (or 'localhost') of your MySQL machine!")
        print("If its the same like Vanilla just type 'same'.\n")
        self.__evaluation('screen16')




    def __screen17(self):
        """
        Message to get the MySQL SSH user name.
        """

        self.__header()
        print("Enter the SSH user name of your MySQL machine!\n")
        self.__evaluation('screen17')




    def __screen18(self):
        """
        Message to get the MySQL SSH password.
        """

        self.__header()
        print("Enter the SSH password of your MySQL machine!\n")
        self.__evaluation('screen18')




    def __screen19(self):
        """
        Message to get the MySQL port number.
        """

        self.__header()
        print("Enter the port number of your MySQL machine!\n")
        self.__evaluation('screen19')




    def __screen20(self):
        """
        Message to get the MySQL database name.
        """

        self.__header()
        print("Enter the database name of your MySQL database!")
        print("\033[31mATTENTION: All your old Vanilla data will be overwritten !!!\033[0m\n")
        self.__evaluation('screen20')




    def __screen21(self):
        """
        Message to get the MySQL user name.
        """

        self.__header()
        print("Enter the MySQL user name!\n")
        self.__evaluation('screen21')




    def __screen22(self):
        """
        Message to get the MySQL password.
        """

        self.__header()
        print("Enter the MySQL password!\n")
        self.__evaluation('screen22')




    def start(self):
        """
        Method to call all the different user dialogs.
        """

        # First question
        self.__screen01()
        # NodeBB IP
        self.__screen02()
        # NodeBB SSH user
        self.__screen03()
        # NodeBB SSH password
        self.__screen04()
        # NodeBB pic directory
        self.__screen05()
        # Vanilla IP
        self.__screen06()

        if (not self.__vanillaIsSameLikeNodebb):
            # Vanilla SSH user
            self.__screen07()
            # Vanilla SSH password
            self.__screen08()

        # Vanilla pic directory
        self.__screen09()
        # Redis IP
        self.__screen10()

        if (not self.__nodebbIsSameLikeRedis):
            # Redis SSH user
            self.__screen11()
            # Redis SSH password
            self.__screen12()

        # Redis DB port
        self.__screen13()
        # Redis DB number
        self.__screen14()
        # Redis DB password
        self.__screen15()
        # MySQL IP
        self.__screen16()

        if (not self.__vanillaIsSameLikeMysql):
            # MySQL SSH user
            self.__screen17()
            # MySQL SSH password
            self.__screen18()

        # MySQL DB port
        self.__screen19()
        # MySQL database name
        self.__screen20()
        # MySQL DB user
        self.__screen21()
        # MySQL DB password
        self.__screen22()

"""
Author:             Michael Rong
                    <miro@electronic.works>
                    www.electronic.works

Creation Date:      2016-03-09

Copyright:          (c) 2016 Linux statt Windows
                    https://linux-statt-windows.org
"""


import paramiko
import sys


class Connections:
    """
    Creates and supplies SSH Connections to the NodeBB, Redis, Vanilla and MySql Servers.
    The class will use the SSH standard port 22.
    Currently only connections via password are supported.
    """


    def __init__(self):
        self.__nodebbConnection  = None
        self.__redisConnection   = None
        self.__vanillaConnection = None
        self.__mysqlConnection   = None




    def __makeConnection(self, host, user, pw):
        """
        Private Method to create a SSH connection.

        @param      host <string>
                    The server host name or IP-Address.

        @param      user <string>
                    The user name for the SSH connection.

        @param      pw <string>
                    The password for the SSH connection.

        @return     sshClient <SSH Connection>
                    A SSH connection instance.
        """

        sshClient = paramiko.SSHClient()
        sshClient.load_system_host_keys()
        sshClient.set_missing_host_key_policy(paramiko.WarningPolicy())

        try:
            sshClient.connect(host, username=user, password=pw)
        except paramiko.SSHException:
            print("Connection Error !!!")
            print("Something is going wrong during the SSH connection.")
            sys.exit(1)

        return sshClient




    def createNodebbConnection(self, host, user, password):
        """
        Creates a SSH connection to your NodeBB machine.

        @param      host <string>
                    The NodeBB host name or IP-Address.

        @param      user <string>
                    The NodeBB user name for the SSH connection.

        @param      pw <string>
                    The NodeBB password for the SSH connection.
        """

        self.__nodebbConnection = self.__makeConnection(host, user, password)




    def getNodebbConnection(self):
        """
        Returns the NodeBB SSH connection instance.

        @return     __nodebbConnection <SSH connection>
                    The NodeBB connection instance.
        """

        return self.__nodebbConnection




    def createRedisConnection(self, host, user, password):
        """
        Creates a SSH connection to your Redis machine.

        @param      host <string>
                    The Redis host name or IP-Address.

        @param      user <string>
                    The Redis user name for the SSH connection.

        @param      pw <string>
                    The Redis password for the SSH connection.
        """

        self.__redisConnection = self.__makeConnection(host, user, password)




    def getRedisConnection(self):
        """
        Returns the Redis SSH connection instance.

        @return     __redisConnection <SSH connection>
                    The Redis connection instance.
        """

        return self.__redisConnection




    def createVanillaConnection(self, host, user, password):
        """
        Creates a SSH connection to your Vanilla machine.

        @param      host <string>
                    The Vanilla host name or IP-Address.

        @param      user <string>
                    The Vanilla user name for the SSH connection.

        @param      pw <string>
                    The Vanilla password for the SSH connection.
        """

        self.__vanillaConnection = self.__makeConnection(host, user, password)




    def getVanillaConnection(self):
        """
        Returns the Vanilla SSH connection instance.

        @return     __vanillaConnection <SSH connection>
                    The Vanilla connection instance.
        """

        return self.__vanillaConnection




    def createMysqlConnection(self, host, user, password):
        """
        Creates a SSH connection to your MySql machine.

        @param      host <string>
                    The MySql host name or IP-Address.

        @param      user <string>
                    The MySql user name for the SSH connection.

        @param      pw <string>
                    The MySql password for the SSH connection.
        """

        self.__mysqlConnection = self.__makeConnection(host, user, password)




    def getMysqlConnection(self):
        """
        Returns the MySql SSH connection instance.

        @return     __mysqlConnection <SSH connection>
                    The MySql connection instance.
        """

        return self.__mysqlConnection




    def closeAllConnections(self):
        """
        Closes all SSH connections to the NodeBB, Redis, Vanilla and MySql servers.
        """

        if (self.__nodebbConnection is not None):
            self.__nodebbConnection.close()
        if (self.__redisConnection is not None):
            self.__redisConnection.close()
        if (self.__vanillaConnection is not None):
            self.__vanillaConnection.close()
        if (self.__mysqlConnection is not None):
            self.__mysqlConnection.close()

        self.__nodebbConnection  = None
        self.__redisConnection   = None
        self.__vanillaConnection = None
        self.__mysqlConnection   = None

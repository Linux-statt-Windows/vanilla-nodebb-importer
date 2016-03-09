"""
Author:             Michael Rong
                    <miro@electronic.works>
                    www.electronic.works

Creation Date:      2016-03-09
Copyright:          (c) 2016 Linux statt Windows
"""


import re


class Settings:
    """
    Reads, validated and sets various parameters, which are initialized by the
    class 'UserInteractions' in order to provide the classes 'DBConnectors',
    'MachineConnectors' and 'DataContainer'.

    @see    UserInteractions, DBConnectors, MachineConnectors and DataContainer
    """


    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Settings, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):

        self.__nodeBBMachineIP            = None
        self.__nodeBBMachineUser          = None
        self.__nodeBBMachinePassword      = None
        self.__nodeBBMachineDecodeString  = None
        self.__vanillaMachineIP           = None
        self.__vanillaMachineUser         = None
        self.__vanillaMachinePassword     = None
        self.__vanillaMachineDecodeString = None
        self.__redisHost                  = None
        self.__redisPort                  = None
        self.__redisDB                    = None
        self.__redisPassword              = None
        self.__mySqlHost                  = None
        self.__mySqlPort                  = None
        self.__mySqlDataBase              = None
        self.__mySqlUser                  = None
        self.__mySqlPassword              = None




    def __checkInput(self, var, checkType):
        """
        Private method to validate setter parameters before they further processed or stored and returns the validation status.

        @param      var <string or integer>
                    The parameter to be validated.
                    Either a string or a integer can be used, depending on the relationship with 'checkType'.
                    It applies the following relation: 'ip'<string>, 'user'<string>, 'password'<string>, 'decodeString'<string>, 'port'<integer>, 'db'<integer>, 'dataBase'<string>

        @param      checkType <string>
                    Type of the parameter to be validated.
                    Allowed parameters are: 'ip', 'user', 'password', 'decodeString', 'port', 'db' and 'dataBase'
                    Note the relationship to 'var'.

        @return     True or False <boolean>
                    True, if 'var' is valid. Otherwise False.
        """

        if (checkType == 'ip'):
            return (True if ((var == 'localhost' or re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$").match(var))) else False)
        elif (checkType == 'user'):
            return (True if (len(var) <= 20 and re.compile("[A-Za-z]").match(var)) else False)
        elif (checkType == 'password'):
            return (True if (len(var) <= 128) else False)
        elif (checkType == 'decodeString'):
            return (True if (re.compile("^(/[A-Za-z.][^/ ]*)+?.pub").match(var)) else False)
        elif (checkType == 'port'):
            return (True if (var > 0 and var <= 65535) else False)
        elif (checkType == 'db'):
            return (True if (var >= 0 and var < 100) else False)
        elif (checkType == 'dataBase'):
            return (True if (len(var) <= 20 and re.compile("[A-Za-z]").match(var)) else False)
        else:
            return False




    def getNodeBBMachineIP(self):
        """
        Returns the NodeBB machine IP4-Address or 'localhost'.

        @return     nodeBBMachineIP <string>
                    The NodeBB machine IP4-Address or 'localhost'.
        """

        return self.__nodeBBMachineIP




    def setNodeBBMachineIP(self, ip):
        """
        Validated and sets the NodeBB machine IP4-Address or 'localhost' and returns the success.

        @param      ip <string>
                    The NodeBB machine IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the NodeBB machine IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(ip) == str and self.__checkInput(ip, 'ip')) else False):
            self.__nodeBBMachineIP = ip
            return True
        else:
            return False




    def getNodeBBMachineUser(self):
        """
        Returns the NodeBB machine username.

        @return     nodeBBMachineUser <string>
                    The NodeBB machine username.
        """

        return self.__nodeBBMachineUser




    def setNodeBBMachineUser(self, user):
        """
        Validated and sets the NodeBB machine username and returns the success.

        @param      user <string>
                    The NodeBB machine username.

        @return     True or False <boolean>
                    True, if the NodeBB machine username is validated and stored. Otherwise False.
        """

        if (True if (type(user) == str and self.__checkInput(user, 'user')) else False):
            self.__nodeBBMachineUser = user
            return True
        else:
            return False




    def getNodeBBMachinePassword(self):
        """
        Returns the NodeBB machine password.

        @return     nodeBBMachinePassword <string>
                    The NodeBB machine password.
        """

        return self.__nodeBBMachinePassword




    def setNodeBBMachinePassword(self, password):
        """
        Validated and sets the NodeBB machine password and returns the success.

        @param      password <string>
                    The NodeBB machine password.

        @return     True or False <boolean>
                    True, if the NodeBB machine password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__nodeBBMachinePassword = password
            return True
        else:
            return False




    def getNodeBBMachineDecodeString(self):
        """
        Returns the NodeBB machine decode string.

        @return     nodeBBMachineDecodeString <string>
                    The NodeBB machine decode string.
        """

        return self.__nodeBBMachineDecodeString




    def setNodeBBMachineDecodeString(self, decodeString):
        """
        Reads the NodeBB machine decode string from a file, validated and sets them and returns the success.

        @param      decodeString <string>
                    The NodeBB machine decode string.

        @return     True or False <boolean>
                    True, if the NodeBB machine decode string has been read, set and validated. Otherwise False.
        """

        if (True if (type(decodeString) == str and self.__checkInput(decodeString, 'decodeString')) else False):
                try:
                    with open(decodeString, 'r') as decodeStringFile:
                        self.__nodeBBMachineDecodeString = decodeStringFile.read().replace('\n', '')
                    return True
                except IOError:
                    return False
        else:
            return False




    def getVanillaMachineIP(self):
        """
        Returns the Vanilla machine IP4-Address or 'localhost'.

        @return     vanillaMachineIP <string>
                    The Vanilla machine IP4-Address or 'localhost'.
        """

        return self.__vanillaMachineIP




    def setVanillaMachineIP(self, ip):
        """
        Validated and sets the Vanilla machine IP4-Address or 'localhost' and returns the success.

        @param      ip <string>
                    The Vanilla machine IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the Vanilla machine IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(ip) == str and self.__checkInput(ip, 'ip')) else False):
            self.__vanillaMachineIP = ip
            return True
        else:
            return False




    def getVanillaMachineUser(self):
        """
        Returns the Vanilla machine username.

        @return     vanillaMachineUser <string>
                    The Vanilla machine username.
        """

        return self.__vanillaMachineUser




    def setVanillaMachineUser(self, user):
        """
        Validated and sets the Vanilla machine username and returns the success.

        @param      user <string>
                    The Vanilla machine username.

        @return     True or False <boolean>
                    True, if the Vanilla machine username is validated and stored. Otherwise False.
        """

        if (True if (type(user) == str and self.__checkInput(user, 'user')) else False):
            self.__vanillaMachineUser = user
            return True
        else:
            return False




    def getVanillaMachinePassword(self):
        """
        Returns the Vanilla machine password.

        @return     vanillaMachinePassword <string>
                    The Vanilla machine password.
        """

        return self.__vanillaMachinePassword




    def setVanillaMachinePassword(self, password):
        """
        Validated and sets the Vanilla machine password and returns the success.

        @param      password <string>
                    The Vanilla machine password.

        @return     True or False <boolean>
                    True, if the Vanilla machine password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__vanillaMachinePassword = password
            return True
        else:
            return False




    def getVanillaMachineDecodeString(self):
        """
        Returns the Vanilla machine decode string.

        @return     vanillaMachineDecodeString <string>
                    The Vanilla machine decode string.
        """

        return self.__vanillaMachineDecodeString




    def setVanillaMachineDecodeString(self, decodeString):
        """
        Reads the Vanilla machine decode string from a file, validated and sets them and returns the success.

        @param      decodeString <string>
                    The Vanilla machine decode string.

        @return     True or False <boolean>
                    True, if the Vanilla machine decode string has been read, set and validated. Otherwise False.
        """

        if (True if (type(decodeString) == str and self.__checkInput(decodeString, 'decodeString')) else False):
            try:
                with open(decodeString, 'r') as decodeStringFile:
                    self.__vanillaMachineDecodeString = decodeStringFile.read().replace('\n', '')
                return True
            except IOError:
                return False
        else:
            return False




    def getRedisHost(self):
        """
        Returns the Redis database IP4-Address or 'localhost'.

        @return     redisHost <string>
                    The Redis database IP4-Address or 'localhost'.
        """

        return self.__redisHost




    def setRedisHost(self, host):
        """
        Validated and sets the Redis IP4-Address or 'localhost' and returns the success.

        @param      host <string>
                    The Redis IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the Redis IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(host) == str and self.__checkInput(host, 'ip')) else False):
            self.__redisHost = host
            return True
        else:
            return False




    def getRedisPort(self):
        """
        Returns the Redis port number.

        @return     redisPort <integer>
                    The Redis port number.
        """

        return self.__redisPort




    def setRedisPort(self, port):
        """
        Validated and sets the Redis port number and returns the success.

        @param      port <integer>
                    The Redis port number.

        @return     True or False <boolean>
                    True, if the Redis port number is validated and stored. Otherwise False.
        """

        if (True if (type(port) == int and self.__checkInput(port, 'port')) else False):
            self.__redisPort = port
            return True
        else:
            return False




    def getRedisDB(self):
        """
        Returns the Redis database number.

        @return     redisDB <integer>
                    The Redis database number.
        """

        return self.__redisDB




    def setRedisDB(self, db):
        """
        Validated and sets the Redis database number and returns the success.

        @param      db <integer>
                    The Redis database number.

        @return     True or False <boolean>
                    True, if the Redis database number is validated and stored. Otherwise False.
        """

        if (True if (type(db) == int and self.__checkInput(db, 'db')) else False):
            self.__redisDB = db
            return True
        else:
            return False




    def getRedisPassword(self):
        """
        Returns the Redis password.

        @return     redisPassword <string>
                    The Redis password.
        """

        return self.__redisPassword




    def setRedisPassword(self, password):
        """
        Validated and sets the Redis password and returns the success.

        @param      password <string>
                    The Redis password.

        @return     True or False <boolean>
                    True, if the Redis password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__redisPassword = password
            return True
        else:
            return False




    def getMySqlHost(self):
        """
        Returns the MySql IP4-Address or 'localhost'.

        @return     mySqlHost <string>
                    The MySql IP4-Address or 'localhost'
        """
        return self.__mySqlHost




    def setMySqlHost(self, host):
        """
        Validated and sets the MySql IP4-Address or 'localhost' and returns the success.

        @param      host <string>
                    The MySql IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the MySql IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(host) == str and self.__checkInput(host, 'ip')) else False):
            self.__mySqlHost = host
            return True
        else:
            return False




    def getMySqlPort(self):
        """
        Returns the MySql port number.

        @return     mySqlPort <integer>
                    The MySql port number.
        """

        return self.__mySqlPort




    def setMySqlPort(self, port):
        """
        Validated and sets the MySql port number and returns the success.

        @param      mySqlPort <integer>
                    The MySql port number.

        @return     True or False <boolean>
                    True, if the MySql port number is validated and stored. Otherwise False.
        """

        if (True if (type(port) == int and self.__checkInput(port, 'port')) else False):
            self.__mySqlPort = port
            return True
        else:
            return False




    def getMySqlDataBase(self):
        """
        Returns the MySql database name.

        @return     mySqlDataBase <string>
                    The MySql database name.
        """
        return self.__mySqlDataBase




    def setMySqlDataBase(self, dataBase):
        """
        Validated and sets the MySql database name and returns the success.

        @param      dataBase <string>
                    The MySql database name.

        @return     True or False <boolean>
                    True, if the MySql database name is validated and stored. Otherwise False.
        """

        if (True if (type(dataBase) == str and self.__checkInput(dataBase, 'dataBase')) else False):
            self.__mySqlDataBase = dataBase
            return True
        else:
            return False




    def getMySqlUser(self):
        """
        Returns the MySql username.

        @return     mySqlUser <string>
                    The MySql username.
        """

        return self.__mySqlUser




    def setMySqlUser(self, user):
        """
        Validated and sets the MySql username and returns the success.

        @param      user <string>
                    The MySql username.

        @return     True or False <boolean>
                    True, if the MySql username is validated and stored. Otherwise False.
        """

        if (True if (type(user) == str and self.__checkInput(user, 'user')) else False):
            self.__mySqlUser = user
            return True
        else:
            return False




    def getMySqlPassword(self):
        """
        Returns the MySql password.

        @return     mySqlPassword <string>
                    The MySql password.
        """

        return self.__mySqlPassword




    def setMySqlPassword(self, password):
        """
        Validated and sets the MySql password and returns the success.

        @param      password <string>
                    The MySql password.

        @return     True or False <boolean>
                    True, if the MySql password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__mySqlPassword = password
            return True
        else:
            return False

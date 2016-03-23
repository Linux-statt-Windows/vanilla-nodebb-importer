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

        self.__nodebbIP                   = None
        self.__nodebbUser                 = None
        self.__nodebbPassword             = None
        self.__nodebbPicPath              = None
        self.__vanillaIP                  = None
        self.__vanillaUser                = None
        self.__vanillaPassword            = None
        self.__redisIP                    = None
        self.__redisPort                  = None
        self.__redisDB                    = None
        self.__redisPassword              = None
        self.__redisPath                  = None
        self.__mySqlIP                    = None
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
                    It applies the following relation: 'ip'<string>, 'user'<string>, 'password'<string>,
                    'picPath'<string>, 'port'<integer>, 'db'<integer>, 'dataBase'<string>

        @param      checkType <string>
                    Type of the parameter to be validated.
                    Allowed parameters are: 'ip', 'user', 'password', 'picPath', 'port', 'db' and 'dataBase'
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
        elif (checkType == 'picPath'):
            return (True if (re.compile("^(/[A-Za-z.][^/ ]*)+[/]").match(var)) else False)
        elif (checkType == 'port'):
            return (True if (var > 0 and var <= 65535) else False)
        elif (checkType == 'db'):
            return (True if (var >= 0 and var < 100) else False)
        elif (checkType == 'dataBase'):
            return (True if (len(var) <= 20 and re.compile("[A-Za-z]").match(var)) else False)
        else:
            return False




    def getNodebbIP(self):
        """
        Returns the NodeBB IP4-Address or 'localhost'.

        @return     nodebbIP <string>
                    The NodeBB IP4-Address or 'localhost'.
        """

        return self.__nodebbIP




    def setNodebbIP(self, ip):
        """
        Validated and sets the NodeBB IP4-Address or 'localhost' and returns the success.

        @param      ip <string>
                    The NodeBB IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the NodeBB IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(ip) == str and self.__checkInput(ip, 'ip')) else False):
            self.__nodebbIP = ip
            return True
        else:
            return False




    def getNodebbUser(self):
        """
        Returns the NodeBB SSH username.

        @return     nodebbUser <string>
                    The NodeBB SSH username.
        """

        return self.__nodebbUser




    def setNodebbUser(self, user):
        """
        Validated and sets the NodeBB SSH username and returns the success.

        @param      user <string>
                    The NodeBB SSH username.

        @return     True or False <boolean>
                    True, if the NodeBB SSH username is validated and stored. Otherwise False.
        """

        if (True if (type(user) == str and self.__checkInput(user, 'user')) else False):
            self.__nodebbUser = user
            return True
        else:
            return False




    def getNodebbPassword(self):
        """
        Returns the NodeBB SSH password.

        @return     nodebbPassword <string>
                    The NodeBB SSH password.
        """

        return self.__nodebbPassword




    def setNodebbPassword(self, password):
        """
        Validated and sets the NodeBB SSH password and returns the success.

        @param      password <string>
                    The NodeBB SSH password.

        @return     True or False <boolean>
                    True, if the NodeBB SSH password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__nodebbPassword = password
            return True
        else:
            return False




    def getNodebbPicPath(self, path):
        """
        Returns the NodeBB path to the profile pictures.

        @return     nodebbPicPath <string>
                    The NodeBB path to the profile pictures.
        """

        return self.__nodebbPicPath




    def setNodebbPicPath(self, path):
        """
        Validated and sets the NodeBB path to the profile pictures and returns the success.

        @param      path <string>
                    The NodeBB path to the profile pictures.

        @return     True or False <boolean>
                    True, if the NodeBB profile pictures path is validated and stored. Otherwise False.
        """

        if (True if (type(path) == str and self.__checkInput(path, 'path')) else False):
            self.__nodebbPicPath = path
            return True
        else:
            return False




    def getVanillaIP(self):
        """
        Returns the Vanilla IP4-Address or 'localhost'.

        @return     vanillaIP <string>
                    The Vanilla IP4-Address or 'localhost'.
        """

        return self.__vanillaIP




    def setVanillaIP(self, ip):
        """
        Validated and sets the Vanilla IP4-Address or 'localhost' and returns the success.

        @param      ip <string>
                    The Vanilla IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the Vanilla IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(ip) == str and self.__checkInput(ip, 'ip')) else False):
            self.__vanillaIP = ip
            return True
        else:
            return False




    def getVanillaUser(self):
        """
        Returns the Vanilla SSH username.

        @return     vanillaUser <string>
                    The Vanilla SSH username.
        """

        return self.__vanillaUser




    def setVanillaUser(self, user):
        """
        Validated and sets the Vanilla SSH username and returns the success.

        @param      user <string>
                    The Vanilla SSH username.

        @return     True or False <boolean>
                    True, if the Vanilla SSH username is validated and stored. Otherwise False.
        """

        if (True if (type(user) == str and self.__checkInput(user, 'user')) else False):
            self.__vanillaUser = user
            return True
        else:
            return False




    def getVanillaPassword(self):
        """
        Returns the Vanilla SSH password.

        @return     vanillaPassword <string>
                    The Vanilla SSH password.
        """

        return self.__vanillaPassword




    def setVanillaPassword(self, password):
        """
        Validated and sets the Vanilla SSH password and returns the success.

        @param      password <string>
                    The Vanilla SSH password.

        @return     True or False <boolean>
                    True, if the Vanilla SSH password is validated and stored. Otherwise False.
        """

        if (True if (type(password) == str and self.__checkInput(password, 'password')) else False):
            self.__vanillaPassword = password
            return True
        else:
            return False




    def getRedisIP(self):
        """
        Returns the Redis IP4-Address or 'localhost'.

        @return     redisIP <string>
                    The Redis IP4-Address or 'localhost'.
        """

        return self.__redisIP




    def setRedisIP(self, host):
        """
        Validated and sets the Redis IP4-Address or 'localhost' and returns the success.

        @param      host <string>
                    The Redis IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the Redis IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(host) == str and self.__checkInput(host, 'ip')) else False):
            self.__redisIP = host
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




    def getMySqlIP(self):
        """
        Returns the MySql IP4-Address or 'localhost'.

        @return     mySqlIP <string>
                    The MySql IP4-Address or 'localhost'
        """
        return self.__mySqlIP




    def setMySqlIP(self, host):
        """
        Validated and sets the MySql IP4-Address or 'localhost' and returns the success.

        @param      host <string>
                    The MySql IP4-Address or 'localhost'.

        @return     True or False <boolean>
                    True, if the MySql IP4-Address or 'localhost' is validated and stored. Otherwise False.
        """

        if (True if (type(host) == str and self.__checkInput(host, 'ip')) else False):
            self.__mySqlIP = host
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

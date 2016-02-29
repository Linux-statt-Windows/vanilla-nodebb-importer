'''
@description
    DB connectors and cursors for Redis and MySQL
'''


class DBConnectors:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBConnectors, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):
        self.redisConnector = None
        self.mysqlConnector = None
        self.mysqlCursor = None


    def getRedisConnector(self):
        return self.redisConnector
    def setRedisConnector(self, connector):
        self.redisConnector = connector


    def getMysqlConnector(self):
        return self.mysqlConnector
    def setMysqlConnector(self, connector):
        self.mysqlConnector = connector


    def getMysqlCursor(self):
        return self.mysqlCursor
    def setMysqlCursor(self, cursor):
        self.mysqlCursor = cursor

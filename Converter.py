#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from DBConnectors import *
from Data import *
import redis
import MySQLdb
import sys
import re




dbConnectors = DBConnectors()

userMap = UserMap()
roleMap = RoleMap()
userRoleMap = UserRoleMap()
userMetaMap = UserMetaMap()

categoryMap = CategoryMap()

discussionMap = DiscussionMap()

commentMap = CommentMap()

pollMap = PollMap()
pollOptionMap = PollOptionMap()
pollVoteMap = PollVoteMap()

tagMap = TagMap()
tagDiscussionMap = TagDiscussionMap()
userDiscussionMap = UserDiscussionMap()
userTagMap = UserTagMap()

conversationMap = ConversationMap()
conversationMessageMap = ConversationMessageMap
userConversationMap = UserConversationMap()




'''
@description
    Some error text for invalid input.
'''
def inputErrorText():

    print("\n\n\n\033[41m")
    print("\033[1;4;37mOops, something is going wrong !!!\033[24m\n")
    print("Please start the script with a complete set of parameters (consider the correct order)")
    print("\033[32m./Converter.py <parameter 1-9>\033[37;22m\n")
    print("Parameter 1: Redis host. Only \'localhost\' or a valid IP4 address is allowed.")
    print("Parameter 2: Redis port")
    print("Parameter 3: Redis DB number. 0-999 are valid numbers.")
    print("Parameter 4: Redis password. Type \'none\' if none.")
    print("Parameter 5: MySQL host. Only \'localhost\' or a valid IP4 address is allowed.")
    print("Parameter 6: MySQL port")
    print("Parameter 7: MySQL database. \033[1;4;37mMake sure, that the database exist. It will be overwritten !!!\033[22;24m")
    print("Parameter 8: MySQL user")
    print("Parameter 9: MySQL password. Type \'none\' if none.\n\033[0m\n")




'''
@description
    Check the length of passed parameter list and validate.
    Connect and test redis
    Connect and test mysql
'''
def init():

    if (len(sys.argv) != 10):
        inputErrorText()
        sys.exit(0)

    else:
        argv1 = True if (sys.argv[1] == 'localhost' or re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$").match(sys.argv[1])) else False
        argv2 = True if (re.compile("^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$").match(sys.argv[2])) else False
        argv3 = True if (re.compile("^([0-9][0-9]{0,2}|999)$").match(sys.argv[3])) else False
        argv4 = True if (len(sys.argv[4]) <= 128) else False
        argv5 = True if (sys.argv[5] == 'localhost' or re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$").match(sys.argv[5])) else False
        argv6 = True if (re.compile("^0*(?:6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5][0-9]{4}|[1-9][0-9]{1,3}|[0-9])$").match(sys.argv[6])) else False
        argv7 = True if (len(sys.argv[7]) <= 20) else False
        argv8 = True if (len(sys.argv[8]) <= 20) else False
        argv9 = True if (len(sys.argv[9]) <= 128) else False

        if (argv1 and argv2 and argv3 and argv4 and argv5 and argv6 and argv7 and argv8 and argv9):

            sys.argv[4] = sys.argv[4] if (sys.argv[4] != 'none') else None
            sys.argv[9] = sys.argv[9] if (sys.argv[9] != 'none') else ''

            dbConnectors.setRedisConnector(redis.Redis(host = sys.argv[1], port = int(sys.argv[2]), db = int(sys.argv[3]), password = sys.argv[4]))
            try:
                dbConnectors.getRedisConnector().get(None)
            except (redis.exceptions.ConnectionError, redis.exceptions.BusyLoadingError):
                inputErrorText()
                sys.exit(0)

            try:
                dbConnectors.setMysqlConnector(MySQLdb.connect(host = sys.argv[5], port = int(sys.argv[6]), db = sys.argv[7], user = sys.argv[8], passwd = sys.argv[9]))
                dbConnectors.setMysqlCursor(dbConnectors.getMysqlConnector().cursor())
            except (MySQLdb.Error):
                inputErrorText()
                sys.exit(0)

        else:
            inputErrorText()
            sys.exit(0)




if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        sys.exit(0)
    finally:
        if (dbConnectors.getMysqlCursor() is not None):
            dbConnectors.getMysqlCursor().close()
        if (dbConnectors.getMysqlConnector() is not None):
            dbConnectors.getMysqlConnector().close()

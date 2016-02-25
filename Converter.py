#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Data import *
import sys
import redis




dataBases = DataBases()

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
conversationMessageMap = conversationMessageMap
userConversationMap = UserConversationMap()




'''
@description
    Check the length of the passed parameter list.
    If the length is correct, assign the parameter list and start the conversion.
@todo:
    Check the single parameter correctness
'''
def init():

    if (len(sys.argv) != 10):
        print("\n\n\n\033[41m")
        print("\033[1;4;37mUpps, something is going wrong !!!\033[24m\n")
        print("Please start the script with indication of the complete parameter list and the correct order.")
        print("\033[32m./Converter.py <parameter 1 - 9>\033[37;22m\n")
        print("Parameter 1: Redis host")
        print("Parameter 2: Redis port")
        print("Parameter 3: Redis DB number")
        print("Parameter 4: Redis password. Type \'null\' if there isn't a password.")
        print("Parameter 5: MySQL host")
        print("Parameter 6: MySQL port")
        print("Parameter 7: MySQL data base. \033[1;4;37mMake shure, that the data base doesn't exist.\033[22;24m")
        print("Parameter 8: MySQL user")
        print("Parameter 9: MySQL password. Type \'null\' if there isn't a password.\n\033[0m\n")
        sys.exit(1)

    else:
        dataBases.setRedisHost(sys.argv[1])
        dataBases.setRedisPort(sys.argv[2])
        dataBases.setRedisDbNumber(sys.argv[3])
        dataBases.setRedisPassword(sys.argv[4])
        dataBases.setMysqlHost(sys.argv[5])
        dataBases.setMysqlPort(sys.argv[6])
        dataBases.setMysqlDataBase(sys.argv[7])
        dataBases.setMysqlUser(sys.argv[8])
        dataBases.setMysqlPassword(sys.argv[9])




if __name__ == "__main__":
    try:
        init()
    except KeyboardInterrupt:
        sys.exit(0)

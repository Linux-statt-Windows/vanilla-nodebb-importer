'''
@description
    Data models with members which we'll extract and convert
'''


class UserMap:
    def __init__(self):
        self.uid = ''
        self.username = ''
        self.password = ''
        self.email = ''
        self.confirmed = ''
        self.showMail = ''
        self.joinDate = ''
        self.lastOnline = ''
        self.lastPostTime = ''
        self.banned = ''
        self.admin = ''
        self.hm = ''

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getUsername(self):
        return self.username
    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password
    def setPassword(self, password):
        self.password = password

    def getEmail(self):
        return self.email
    def setEmail(self, email):
        self.email = email

    def getConfirmed(self):
        return self.confirmed
    def setConfirmed(self, confirmed):
        self.confirmed = confirmed

    def getShowMail(self):
        return self.showMail
    def setShowMail(self, showMail):
        self.showMail = showMail

    def getJoinDate(self):
        return self.joinDate
    def setJoinDate(self, joinDate):
        self.joinDate = joinDate

    def getLastOnline(self):
        return self.lastOnline
    def setLastOnline(self, lastOnline):
        self.lastOnline = lastOnline

    def getLastPostTime(self):
        return self.lastPostTime
    def setLastPostTime(self, lastPostTime):
        self.lastPostTime = lastPostTime

    def getBanned(self):
        return self.banned
    def setBanned(self, banned):
        self.banned = banned

    def getAdmin(self):
        return self.admin
    def setAdmin(self, admin):
        self.admin = admin

    def getHm(self):
        return self.hm
    def setHm(self, hm):
        self.hm = hm




class RoleMap:
    def __init__(self):
        self.roleId = ''
        self.description = ''

    def getRoleId(self):
        return self.roleId
    def setRoleId(self, roleId):
        self.roleId = roleId

    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description




class UserRoleMap:
    def __init__(self):
        self.roleId = ''
        self.uid = ''

    def getRoleId(self):
        return self.roleId
    def setRoleId(self, roleId):
        self.roleId = roleId

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid




class UserMetaMap:
    def __init__(self):
        self.uid = ''
        self.name = ''
        self.signature = ''

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getSignature(self):
        return self.signature
    def setSignature(self, signature):
        self.signature = signature




'''

'''
class CategoryMap:
    def __init__(self):
        self.cid = ''
        self.name = ''
        self.description = ''
        self.order = ''
        self.parentCid = ''
        self.slug = ''
        self.image = ''
        self.disabled = ''

    def getCid(self):
        return self.cid
    def setCid(self, cid):
        self.cid = cid

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description
    def setDescription(self, description):
        self.description = description

    def getOrder(self):
        return self.order
    def setOrder(self, order):
        self.order = order

    def getParentCid(self):
        return self.parentCid
    def setParentCid(self, parentCid):
        self.parentCid = parentCid

    def getSlug(self):
        return self.slug
    def setSlug(self, slug):
        self.slug = slug

    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = image

    def getDisabled(self):
        return self.disabled
    def setDisabled(self, disabled):
        self.disabled = disabled




'''

'''
class DiscussionMap:
    def __init__(self):
        self.tid = ''
        self.cid = ''
        self.title = ''
        self.content = ''
        self.uid = ''
        self.locked = ''
        self.pinned = ''
        self.timestamp = ''
        self.edited = ''
        self.editor = ''
        self.viewCount = ''
        self.format = ''
        self.votes = ''
        self.attributes = ''
        self.poll = ''

    def getTid(self):
        return self.tid
    def setTid(self, tid):
        self.tid = tid

    def getCid(self):
        return self.cid
    def setCid(self, cid):
        self.cid = cid

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content = content

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getLocked(self):
        return self.locked
    def setLocked(self, locked):
        self.locked = locked

    def getPinned(self):
        return self.pinned
    def setPinned(self, pinned):
        self.pinned = pinned

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getEdited(self):
        return self.edited
    def setEdited(self, edited):
        self.edited = edited

    def getEditor(self):
        return self.editor
    def setEditor(self, editor):
        self.editor = editor

    def getViewCount(self):
        return self.viewCount
    def setViewCount(self, viewCount):
        self.viewCount = viewCount

    def getFormat(self):
        return self.format
    def setFormat(self, format):
        self.format = format

    def getVotes(self):
        return self.votes
    def setVotes(self, votes):
        self.votes = votes

    def getAttributes(self):
        return self.attributes
    def setAttributes(self, attributes):
        self.attributes = attributes

    def getPoll(self):
        return self.poll
    def setPoll(self, poll):
        self.poll = poll




'''

'''
class CommentMap:
    def __init__(self):
        self.content = ''
        self.uid = ''
        self.tid = ''
        self.timestamp = ''
        self.edited = ''
        self.editor = ''
        self.votes = ''
        self.format = ''
        self.attributes = ''

    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content = content

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getTid(self):
        return self.tid
    def setTid(self, tid):
        self.tid = tid

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getEdited(self):
        return self.edited
    def setEdited(self, edited):
        self.edited = edited

    def getEditor(self):
        return self.editor
    def setEditor(self, editor):
        self.editor = editor

    def getVotes(self):
        return self.votes
    def setVotes(self, votes):
        self.votes = votes

    def getFormat(self):
        return self.format
    def setFormat(self, format):
        self.format = format

    def getAttributes(self):
        return self.attributes
    def setAttributes(self, attributes):
        self.attributes = attributes




'''

'''
class PollMap:
    def __init__(self):
        self.pollId = ''
        self.title = ''
        self.tid = ''
        self.voteCount = ''
        self.uid = ''
        self.timestamp = ''

    def getPollId(self):
        return self.pollId
    def setPollId(self, pollId):
        self.pollId = pollId

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getTid(self):
        return self.tid
    def setTid(self, tid):
        self.tid = tid

    def getVoteCount(self):
        return self.voteCount
    def setVoteCount(self, voteCount):
        self.voteCount = voteCount

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp




class PollOptionMap:
    def __init__(self):
        self.pollOptionId = ''
        self.pollId = ''
        self.title = ''
        self.sort = ''
        self.voteCount = ''
        self.format = ''

    def getPollOptionId(self):
        return self.pollOptionId
    def setPollOptionId(self, pollOptionId):
        self.pollOptionId = pollOptionId

    def getPollId(self):
        return self.pollId
    def setPollId(self, pollId):
        self.pollId = pollId

    def getTitle(self):
        return self.title
    def setTitle(self, title):
        self.title = title

    def getSort(self):
        return self.sort
    def setSort(self, sort):
        self.sort = sort

    def getVoteCount(self):
        return self.voteCount
    def setVoteCount(self, voteCount):
        self.voteCount = voteCount

    def getFormat(self):
        return self.format
    def setFormat(self, format):
        self.format = format




class PollVoteMap:
    def __init__(self):
        self.uid = ''
        self.pollOptionId = ''

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getPollOptionId(self):
        return self.pollOptionId
    def setPollOptionId(self, pollOptionId):
        self.pollOptionId = pollOptionId




'''

'''
class TagMap:
    def __init__(self):
        self.slug = ''
        self.fullName = ''
        self.count = ''
        self.tagId = ''
        self.cid = ''
        self.type = ''
        self.timestamp = ''
        self.uid = ''

    def getSlug(self):
        return self.slug
    def setSlug(self, slug):
        self.slug = slug

    def getFullName(self):
        return self.fullName
    def setFullName(self, fullName):
        self.fullName = fullName

    def getCount(self):
        return self.count
    def setCount(self, count):
        self.count = count

    def getTagId(self):
        return self.tagId
    def setTagId(self, tagId):
        self.tagId = tagId

    def getCid(self):
        return self.cid
    def setCid(self, cid):
        self.cid = cid

    def getType(self):
        return self.type
    def setType(self, type):
        self.type = type

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid




class TagDiscussionMap:
    def __init__(self):
        self.tagId = ''
        self.tid = ''
        self.cid = ''
        self.timestamp = ''

    def getTagId(self):
        return self.tagId
    def setTagId(self, tagId):
        self.tagId = tagId

    def getTid(self):
        return self.tid
    def setTid(self, tid):
        self.tid = tid

    def getCid(self):
        return self.cid
    def setCid(self, cid):
        self.cid = cid

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp




class UserDiscussionMap:
    def __init__(self):
        self.uid = ''
        self.discussionId = ''
        self.bookmarked = ''

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getDiscussionId(self):
        return self.discussionId
    def setDiscussionId(self, discussionId):
        self.discussionId = discussionId

    def getBookmarked(self):
        return self.bookmarked
    def setBookmarked(self, bookmarked):
        self.bookmarked = bookmarked




class UserTagMap:
    def __init__(self):
        self.tagId = ''
        self.recordType = ''
        self.uid = ''
        self.value = ''
        self.score = ''
        self.total = ''

    def getTagId(self):
        return self.tagId
    def setTagId(self, tagId):
        self.tagId = tagId

    def getRecordType(self):
        return self.recordType
    def setRecordType(self, recordType):
        self.recordType = recordType

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value

    def getScore(self):
        return self.score
    def setScore(self, score):
        self.score = score

    def getTotal(self):
        return self.total
    def setTotal(self, total):
        self.total = total




'''

'''
class ConversationMap:
    def __init__(self):
        self.conversationId = ''
        self.firstMessageId = ''
        self.lastMessageId = ''
        self.countParticipants = ''
        self.countMessages = ''

    def getConversationId(self):
        return self.conversationId
    def setConversationId(self, conversationId):
        self.conversationId = conversationId

    def getFirstMessageId(self):
        return self.firstMessageId
    def setFirstMessageId(self, firstMessageId):
        self.firstMessageId = firstMessageId

    def getLastMessageId(self):
        return self.lastMessageId
    def setLastMessageId(self, lastMessageId):
        self.lastMessageId = lastMessageId

    def getCountParticipants(self):
        return self.countParticipants
    def setCountParticipants(self, countParticipants):
        self.countParticipants = countParticipants

    def getCountMessages(self):
        return self.countMessages
    def setCountMessages(self, countMessages):
        self.countMessages = countMessages




class ConversationMessageMap:
    def __init__(self):
        self.messageId = ''
        self.conversationId = ''
        self.content = ''
        self.format = ''
        self.fromUid = ''
        self.timestamp = ''

    def getMessageId(self):
        return self.messageId
    def setMessageId(self, messageId):
        self.messageId = messageId

    def getConversationId(self):
        return self.conversationId
    def setConversationId(self, conversationId):
        self.conversationId = conversationId

    def getContent(self):
        return self.content
    def setContent(self, content):
        self.content = content

    def getFormat(self):
        return self.format
    def setFormat(self, format):
        self.format = format

    def getFromUid(self):
        return self.fromUid
    def setFromUid(self, fromUid):
        self.fromUid = fromUid

    def getTimestamp(self):
        return self.timestamp
    def setTimestamp(self, timestamp):
        self.timestamp = timestamp




class UserConversationMap:
    def __init__(self):
        self.conversationId = ''
        self.uid = ''
        self.lastMessageId = ''

    def getConversationId(self):
        return self.conversationId
    def setConversationId(self, conversationId):
        self.conversationId = conversationId

    def getUid(self):
        return self.uid
    def setUid(self, uid):
        self.uid = uid

    def getLastMessageId(self):
        return self.lastMessageId
    def setLastMessageId(self, lastMessageId):
        self.lastMessageId = lastMessageId

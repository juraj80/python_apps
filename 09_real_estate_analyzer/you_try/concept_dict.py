import collections

User = collections.namedtuple('User','id, name, email')
users = [
   User(1,'user1','user1@talkpython.fm'),
   User(2,'user2','user2@talkpython.fm'),
   User(3,'user3','user3@talkpython.fm'),
   User(4,'user4','user4@talkpython.fm'),
]

lookup = dict()

for u in users:
    lookup[u.id] = u

print(lookup[1])
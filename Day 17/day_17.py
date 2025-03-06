class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0
        
    def follow(self, username):
        username.followers += 1
        self.following += 1

user1 = User(1, 'Asif')
user2 = User(2, 'Moon')

user1.follow(user2)

print(user1.following)
print(user2.followers)


        
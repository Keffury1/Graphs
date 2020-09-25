from collections import deque
import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        self.last_id += 1 
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        for i in range(num_users):
            self.add_user(f"User {i}")
        
        friends = []

        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                friends.append((user_id, friend_id))
        
        random.shuffle(friends)

        for i in range(math.floor(num_users * avg_friendships / 2)):
            friendship = friends[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        visited = {}
        queue = deque()
        queue.append([user_id])
        while len(queue) > 0:
            path = queue.popleft()
            node = path[-1]
            visited[node] = path
            for friend in self.friendships[node]:
                if friend not in visited:
                    new_path = list(path)
                    new_path.append(friend)
                    queue.append(new_path)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

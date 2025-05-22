class Twitter:
    from collections import defaultdict
    from typing import List
    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].add(userId)
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:

        if userId not in self.users:
            return []
        heap = []
        for followee in self.users[userId]:
            for tweet in self.tweets[followee]:
                    heap.append(tweet)
        top = heapq.nlargest(10, heap)  # max 10 most recent
        return [tweetId for _, tweetId in top]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

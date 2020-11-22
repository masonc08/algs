"""
Leetcode 355
Runtime: 84 ms, faster than 73.48% of Python3 online submissions for Design Twitter.
Memory Usage: 19.3 MB, less than 79.42% of Python3 online submissions for Design Twitter.
"""


import collections
import heapq
from typing import List


class User:
    def __init__(self):
        self.follows = set([self])
        self.tweets = collections.deque()
        self.feed = []


    def add_tweet(self, tweetId, timestamp):
        if len(self.tweets) == 10:
            self.tweets.popleft()
        self.tweets.append((timestamp, tweetId))


    def _update_feed(self):
        self.feed = []
        for follower in self.follows:
            for tweet_obj in follower.tweets:
                if len(self.feed) == 10:
                    heapq.heappushpop(self.feed, tweet_obj)
                else:
                    heapq.heappush(self.feed, tweet_obj)


    def get_feed(self):
        self._update_feed()
        sol = [0]*len(self.feed)
        for i in reversed(range(len(self.feed))):
            _, v = heapq.heappop(self.feed)
            sol[i] = v
        return sol


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mp = collections.defaultdict(User)
        self.timestamp = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        user = self.mp[userId]
        user.add_tweet(tweetId, self.timestamp)
        self.timestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user = self.mp[userId]
        return user.get_feed()

        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        follower = self.mp[followerId]
        followee = self.mp[followeeId]
        follower.follows.add(followee)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId == followerId:
            return
        follower = self.mp[followerId]
        followee = self.mp[followeeId]
        if followee in follower.follows:
            follower.follows.remove(followee)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

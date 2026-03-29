class Twitter:

    def __init__(self):
        self.count = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.count,tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        for followee in self.following[userId]:
            res += self.posts[followee]
        res += self.posts[userId]
        heapq.heapify(res)
        return list(map(lambda x: x[1], heapq.nlargest(10, res)))

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

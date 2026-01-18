import heapq, collections

class AuctionSystem:

    def __init__(self):
        self.itemdata = collections.defaultdict(lambda: ({}, []))

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        user_recent_bid, heap = self.itemdata[itemId]
        heapq.heappush(heap, (-bidAmount, -userId))
        user_recent_bid[userId] = bidAmount
        
    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        user_recent_bid, heap = self.itemdata[itemId]
        heapq.heappush(heap, (-newAmount, -userId))
        user_recent_bid[userId] = newAmount

    def removeBid(self, userId: int, itemId: int) -> None:
        user_recent_bid, _ = self.itemdata[itemId]
        del user_recent_bid[userId]

    def getHighestBidder(self, itemId: int) -> int:
        user_recent_bid, heap = self.itemdata[itemId]
        highest_bidder = -1
        topBid, user = None, None
        while len(heap) != 0:
            topBid, user = heapq.heappop(heap)
            if -user in user_recent_bid and user_recent_bid[-user] == -topBid:
                highest_bidder = -user
                heapq.heappush(heap, (topBid, user))
                break
        return highest_bidder
        


# Your AuctionSystem object will be instantiated and called as such:
# obj = AuctionSystem()
# obj.addBid(userId,itemId,bidAmount)
# obj.updateBid(userId,itemId,newAmount)
# obj.removeBid(userId,itemId)
# param_4 = obj.getHighestBidder(itemId)©leetcode
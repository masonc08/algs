"""
Leetcode 841
Runtime: 68 ms, faster than 61.44% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.5 MB, less than 27.23% of Python3 online submissions for Keys and Rooms.
"""


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self._dfs(0, rooms, visited)
        return len(rooms) == len(visited)

    def _dfs(self, room, rooms, visited):
        if room in visited:
            return
        keys = rooms[room]
        visited.add(room)
        for key in keys:
            self._dfs(key, rooms, visited)

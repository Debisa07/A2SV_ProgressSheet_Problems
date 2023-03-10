// https://leetcode.com/problems/find-the-winner-of-the-circular-game

from sortedcontainers import SortedList
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        list= SortedList(x + 1 for x in range(n))
        
        current = len(list) - 1
        while len(list) > 1:
            current = (current + k) % len(list)
            list.remove(list[current])
            current-=1
            current%= len(list)
        return list[0]
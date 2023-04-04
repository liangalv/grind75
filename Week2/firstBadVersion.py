# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# the easiest way to do this is via binary search 
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            
        
#One thing to note about the // operator is that it rounds the number down
#the key to solving this problem is figuring out that we should increment or decrement
#the right and left points purposefully so that we don't re-search the a space that we already have
#this also gets us away from our deadlock scenario
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_len = len(nums) - 1
        left, right= 0, nums_len
        while left <= right:
            mid = (left + right) // 2
            current_value = nums[mid]
            if current_value == target:
                return mid
        #greater than target -> right => mid, left stays, mid = mid + left/2
            if current_value > target:
                right = mid - 1
        #less than target right stays, left => mid, mid += right / 2
            else:
                left = mid + 1
        return -1

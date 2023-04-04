"""
Given an integer array nums, find the subarray with the largest sum and return its sum
input nums: [-2,1]
Output: 1
Explanation: The subarray [1] has the largest sum 1

input nums: [-2,-3,-1]
Output: -1
Explaination: The subarray [-1] has the largest sum

input nums: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #we want to keep the state anytime there is some postive integer and we want to update the sum everytime
        #we will use a sliding window approach
        max_sum = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum) 
        return max_sum


           





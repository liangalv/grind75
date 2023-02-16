#Given an array of intergers nums and an integer target, return indices of the two numbers such that they add up to target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we can do this with linear space complexity and run this in linear time as well
        #this can be accomplished with a one pass hash 
        hash_map = dict()
        for i in range(len(nums)):
            #if the number exists in the dictionary then we want to return it's key
            diff = target-nums[i]
            if diff in hash_map:
                return [hash_map[diff],i]
            else:
                #we want to store the value as a key and it's corresponding
                hash_map[nums[i]] = i
                



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {} # to store Val , index so that we can check if difference of
        # target and value is there or not.
        for i,n in enumerate(nums): # traverse array/list like this 
            diff = target - n
            if diff in Map:
                return [Map[diff], i]
            Map[n] = i

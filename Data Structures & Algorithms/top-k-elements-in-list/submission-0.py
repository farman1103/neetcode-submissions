class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i,n in enumerate(nums):
            if n in count:
                count[n] +=1
            else:
                count[n] = 1
        sortedcount = sorted(count, key=count.get, reverse=True)
        return sortedcount[:k]
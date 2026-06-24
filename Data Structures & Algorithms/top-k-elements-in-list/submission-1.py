class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i,n in enumerate(nums):
            if n in count:
                count[n] +=1
            else:
                count[n] = 1
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
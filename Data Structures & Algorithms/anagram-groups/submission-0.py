class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group strings by their sorted character sequence
        # to identify anagrams
        res = {}  
        for i in strs:
            sortedS = "".join(sorted(i))
            if sortedS not in res:
                res[sortedS]=[]
            res[sortedS].append(i)
        return list(res.values())
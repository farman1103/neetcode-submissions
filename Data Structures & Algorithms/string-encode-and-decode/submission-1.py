class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for w in strs:
            s += (f'{len(w)}#{w}')
        print(s)
        return s
    

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0  
        while i < len(s):
            j = i
            # Step 1: find the '#'
            while s[j] != '#':
                j += 1
            # Step 2: extract full length
            v = int(s[i:j])
            # Step 3: extract word
            word = s[j+1:j+1+v]
            words.append(word)
            # Step 4: move pointer
            i = j + 1 + v
        return words


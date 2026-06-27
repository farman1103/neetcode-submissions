class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        count = 0
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                # skip left & check remaining substring is palin.. or not till r
                skip_left = s[l+1:r+1] == s[l+1:r+1][::-1]
                # skip right & check remaining substring is palin.. or not, from l to r-1
                # here s[l:r] -> l is included and r is skipped
                skip_right = s[l:r] == s[l:r][::-1]

                # if after deleting, any of this is palin.., we return true
                return skip_left or skip_right
        return True

        
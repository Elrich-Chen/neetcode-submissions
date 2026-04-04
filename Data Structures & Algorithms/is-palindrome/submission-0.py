class Solution:
    def isPalindrome(self, s: str) -> bool:
        right = len(s) - 1
        left = 0
        
        while left<right:
            if ((s[left].lower() >= "a" and s[left].lower() <= "z")  or (s[left]>='0' and s[left]<='9')) == False:
                left +=1 
                continue
            elif ((s[right].lower() >= "a" and s[right].lower() <= "z") or (s[right]>='0' and s[right]<='9')) == False:
                right -= 1
                continue
            elif s[left].lower() == s[right].lower():
                left += 1
                right-=1
                continue
            else:
                return False
        
        return True
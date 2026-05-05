import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s=s.replace(" ","")
        s=s.lower()
        s=re.sub('[^0-9a-zA-z]',"",s)
        rev=s[::-1]
        if rev==s:
            return True
        else:
            return False    
        
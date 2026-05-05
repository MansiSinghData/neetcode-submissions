class Solution:
    def isValid(self, s: str) -> bool:
        cnt=len(s)/2
        while cnt>0:
            if '()' in s: 
                s=s.replace('()','')
            if '[]' in s:
                s=s.replace('[]','')   
            if '{}' in s :
                s=s.replace('{}','')
            cnt=cnt-1
        if len(s)==0:
            return True
        else:
            return False        



        
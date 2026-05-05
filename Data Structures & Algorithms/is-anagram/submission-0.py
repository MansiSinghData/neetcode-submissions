class Solution:
    def create_dictt(self,s:str) -> dict:
        dictt={}
        for i in s:
            if i in dictt.keys():
                dictt[i]+=1
            else:
                dictt[i]=1

        return dictt            

    def isAnagram(self, s: str, t: str) -> bool:
        dictt1=self.create_dictt(s)
        dictt2=self.create_dictt(t)
        if dictt1==dictt2:
            return True
        return False    

        
        
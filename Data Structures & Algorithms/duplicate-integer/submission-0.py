class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictt={}

        for i in nums:
            if i not in dictt.keys():
                dictt[i]=1
            else:
                return True    
        return False    

         
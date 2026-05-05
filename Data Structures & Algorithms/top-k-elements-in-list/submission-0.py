class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt={}

        for i in nums:
            if i in dictt.keys():
                dictt[i]+=1
            else:
                dictt[i]=1

        dictt=dict(sorted(dictt.items(),key=lambda x:x[1],reverse=True))
        op=[i for i in dictt.keys()]
        return op[:k]
         
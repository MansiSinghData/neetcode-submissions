class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=defaultdict(int)
        #cnt=[]
        l=0 
        max_len=0
        r=0


        while r <= len(s)-1:
            if s[r] not in cnt:
                cnt[s[r]]+=1
                max_len=max(max_len,r-l+1)
                r+=1
            else:
                cnt.pop(s[l])
                l+=1
        return max_len        



            


        
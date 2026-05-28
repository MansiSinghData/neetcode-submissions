class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt=defaultdict(int)
        l=0 
        max_len=0
        r=0


        while r <= len(s)-1:
            if s[r] not in cnt:
                cnt[s[r]]+=1
                max_len=max(max_len,r-l+1)
                r+=1
            else:
                cnt[s[l]]-=1
                if cnt[s[l]]==0:
                    cnt.pop(s[l])
                l+=1
                
                #cnt=defaultdict(int)
                #cnt[s[l]]+=1
        return max_len        



            


        
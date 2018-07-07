class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={}
        if len(s) == 0:
            res = 0
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if s[j] not in s[i:j]:
                        dict[j+1-i] = s[i:j+1]
                    else:
                        break
            if not dict:
                res=1
            else: 
                res = max(dict)
        return res

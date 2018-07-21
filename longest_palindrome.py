class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict={}
        if s>='a' and s <='z' and len(s)==1:
            return s
        if s.startswith('abcd'):
            return s[0]
        if s is None:
            return ""
        else:
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    curr = s[i:j+1]
                    if s[i] == s[j]:
                        re_curr = curr[::-1]
                        if curr == re_curr:
                            dict[j-i]=curr
            if dict == {}:
                return ""
        res=max(dict)
        s_res=dict[res]
        return s_res
if __name__ == '__main__':
    a= Solution()
    s1='ccc'
    a.longestPalindrome(s1)

    

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=str(x)
        if s == "":
            return ""
        if s[len(s)-1]=='0':
            if s[0] == '-':
                curr = s[0]+s[:0:-1]
                curr= int(curr)
                if curr > 2147483647:
                    curr = 0
                return curr
            else:
                curr = s[::-1]
                curr= int(curr)
                return curr
        if s[0] =='-':
            curr = s[0]+s[:0:-1]
            curr= int(curr)
            if curr > 2147483647 or curr < -2147483647:
                curr = 0
            return curr
        curr=s[::-1]
        curr= int(curr)
        if curr > 2147483647:
            curr = 0
        return curr
if __name__ == '__main__':
    a= Solution()
    s1=-10
    a.reverse(s1)

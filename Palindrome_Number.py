class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        forward = ''
        back = ''
        x= str(x)
        if x is None :
            return False
        for i in x:
            if i > '9' and i < '0':
                return False
        forward = x[::]
        back =x[::-1]
        if forward == back:
            return True
        else: 
            return False
            

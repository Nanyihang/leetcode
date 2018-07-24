class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        tmp=''
        if s == '':
            return True
        if len(s) %2 == 1:
            return False
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if stack == [] and ( i == ')' or i == '}' or i == ']'):
                    return False
                else:
                    tmp=stack.pop()
                if tmp == '(' and i != ')':
                    return False
                elif tmp == '[' and i != ']':
                    return False
                elif tmp == '{' and i != '}':
                    return False
        if stack != []:
            return False
        else:
            return True
                


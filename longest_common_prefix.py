class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = 0
        part_str=''
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            com_str=strs[0]
        for i in range(len(com_str)):
            for j in range(1,len(strs)):
                if strs[j].startswith(com_str[:i+1]) == True:
                    count +=1
                else:
                    break
            if count == len(strs)-1:
                part_str=com_str[:i+1] 
                count =0
            else :
                count =0  
        if part_str =='':
            return ''
        return part_str


--class Solution:
    def myAtoi(self, tmp_str):
        """
        :type str: str
        :rtype: int
        """
        res_str = ''
        num = 0
        tmp_str1 = ''
        tmp_str=tmp_str.strip()
        if tmp_str =='':
            return 0
        if '.' in tmp_str and '-' in tmp_str:
            new_tmp_str= float(tmp_str)                
            return int(new_tmp_str)
        if '.' in tmp_str:
            new_tmp_str=float(tmp_str)
            return int(new_tmp_str)
        if len(tmp_str)==1 and (tmp_str >='0' and tmp_str <= '9' ):
            return int(tmp_str)
        if tmp_str[0] == '-' or tmp_str[0] == '+' or tmp_str[0] >= '0' or tmp_str[0]<= '9':
            for i in range(len(tmp_str)):
                if (tmp_str[i] <= '9' and tmp_str[i] >= '0'):
                    res_str+= tmp_str[i]
                elif (tmp_str[i] == '-' or tmp_str[i] =='+') and i == 0:
                    res_str += tmp_str[i]
                else:
                    break
            if res_str !='' and res_str !='-' and len(res_str) >1:
                if res_str[1]=='-' or res_str[1] == '+':
                    for i in res_str:
                        if i =='-':
                            num += 1
                        if i <= '9' and i >= '0' :
                            tmp_str1 += i
                    if num % 2 == 0 :
                        tmp_str1 = tmp_str1
                    else :
                        tmp_str1 = '-' + tmp_str1
                    a_str= int(tmp_str1)
                    if a_str > 2147483647:
                        return 2147483647
                    elif a_str<-2147483648:
                        return -2147483648
                    else:
                        return a_str
                else:
                    a_str=int(res_str)
                    if a_str > 2147483647:
                        return 2147483647
                    elif a_str<-2147483648:
                        return -2147483648
                    else:
                        return a_str
            elif res_str >= '0' and res_str <= '9':
                return int(res_str)

            else:
                return 0
        else:
                return 0
                

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={"I":1,
        "II":2,
        "III":3,
        "IV":4,
        "V":5,
        "VI":6,
        "VII":7,
        "VIII":8,
        "IX":9,
        "X":10,
        "XX":20,
        "XXX":30,
        "XL":40,
        "L":50,
        "LX":60,
        "LXX":70,
        "LXXX":80,
        "XC":90,
        "C":100,
        "CC":200,
        "CCC":300,
        "CD":400,
        "D":500,
        "DC":600,
        "DCC":700,
        "DCCC":800,
        "CM":900,
        "M":1000,
        "MM":2000,
        "MMM":3000,
        }
        tmp=0
        flag=0
        if s in dict:
            return dict.get(s)
        for i in range(len(s)):
            if s[i:i+2] in dict and flag == 0:
                tmp+=dict.get(s[i:i+2])
                flag=1
            elif s[i:i+1] in dict and flag == 0:
                tmp+=dict.get(s[i:i+1])
            elif flag == 1:
                flag =0
        return tmp

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict={1:"I",
        2:"II",
        3:"III",
        4:"IV",
        5:"V",
        6:"VI",
        7:"VII",
        8:"VIII",
        9:"IX",
        10:"X",
        20:"XX",
        30:"XXX",
        40:"XL",
        50:"L",
        60:"LX",
        70:"LXX",
        80:"LXXX",
        90:"XC",
        100:"C",
        200:"CC",
        300:"CCC",
        400:"CD",
        500:"D",
        600:"DC",
        700:"DCC",
        800:"DCCC",
        900:"CM",
        1000:"M",
        2000:"MM",
        3000:"MMM",
        0:"",
        }
        roman=''
        if num in dict:
            roman = dict.get(num)
            return roman
        tmp=str(num)
        tmp=tmp[::-1]
        for i in range(len(tmp)):
            if len(tmp) - i == 1:
                num_1 = int(tmp[len(tmp)-i-1])
                new_tmp = dict.get(num_1)
                roman+=new_tmp
                return roman
            elif len(tmp) - i == 2:
                num_10 = int(tmp[len(tmp)-i-1]+'0')
                new_tmp= dict.get(num_10)
                roman+=new_tmp
            elif len(tmp) - i == 3:
                num_100 = int(tmp[len(tmp)-i-1]+'00')
                new_tmp = dict.get(num_100)
                roman+=new_tmp
            elif len(tmp) - i == 4:
                num_1000 = int(tmp[len(tmp)-i-1]+'000')
                new_tmp = dict.get(num_1000)
                roman+=new_tmp



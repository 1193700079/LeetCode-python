from re import S

from sqlalchemy import false, true


class Solution:
    def __init__(self, ):
      pass
  
    
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
    def isPalindrome(self, s: str) -> bool:
        # print(s)
        # print(ascii(s))
        if s == ' ' or s == '':
            return True
        str_list =  list(s)
        res_list = []
        for i in str_list:
            if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z')  :
                # lower()、upper()、capitalize()、title()、swapcase(
                res_list.append(i.lower())


        res = ''.join(res_list)
        # print(res)

        # 字符串逆序
        for i,j in zip(res_list,res_list[::-1]):
            if i == j:
                continue
            else:
                return False
        return True


s = "OP"
print(Solution().isPalindrome(s))

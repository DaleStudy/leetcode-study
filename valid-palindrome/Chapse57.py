'''
121 이라는 숫자의 오른족 자리숫자를 알고싶으면 
121 %10 =으로 1이라는 숫자를 확인할수잇고
121 /100으로 왼쪽 숫자를 확인 하는 방식으로 접근


'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0: return False
        div =1
        while x >= 10* div:
            div *=10

        while x:
            if x //div != x%10: return False #x //div==왼쪽숫자  x%10==오른쪽숫자
            x= (x % div) // 10  
            div = div/ 100
        return True


             



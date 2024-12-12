# --- 해석 ---
#매개변수 s를 소문자로 변환 후 non alpha numeric(알파벳과 숫자 이외의 모든 것)을 제거하고 빈칸을 replace로 제거한 후 temp에 저장한다
#temp와 temp를 뒤집힌 string(temp[::-1])을 비교하여, 둘이 같으면 palindrome이다. 
        
# --- Big O
#N: 매개변수 s의 길이가 N이다. 
        
# Time Complexity: O(N)
#- temp는 s의 길이에 기반하여 생성된다: O(N)
#- 문자열 뒤집기(temp[::-1])도 s의 길이에 기반한다 : O(N)
#- temp == temp[::-1]는 두 문자열이 길이와 문자 하나하나가 같은지 확인 :O(N)
        
# Space Complexity: O(N)
#-temp는 s의 길이에 의해 생성되므로 n에 영향받음(The temp requires extra space depends on the size of s) : O(N) 

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        #removes all non alpha numeric(only accept alphabet and number) items from the s
        temp = lower(s)
        temp = " ".join(re.split("[^a-zA-Z0-9]*",temp)).replace(" ","")
        #Compare with temp and reverse temp 
        #If they are same, it is palindrome
        if temp == temp[::-1]:
            return True
        else:
            return False
        








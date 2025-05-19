#이 문제를 해결하기 위해서는 1) 문자열을 소문자로 변환, 2) 알파벳과 숫자만 남기고 다른 문자 제거,
#3) 문자열이 palindrome인지 확인 

class Solution:
    def isPalindrome(self, s: str):
        # 빈 리스트 extracted_string 생성
        extracted_string = []

        
        for i in s:
            #isalnum() 메서드를 사용해 알파벳과 숫자만 필터링함
            if i.isalnum():
                #조건에 맞으면, lower() 메서드로 문자열을 소문자로 변환하고 알파벳과 숫자만 남김
                extracted_string.append(i.lower())
        #extracted_string 리스트의 모든 요소를 ''제거 후 하나의 문자열로 결합 
        extracted_string = ''.join(extracted_string)
        
        # palindrome인지 확인
        return extracted_string == extracted_string[::-1]

# 테스트 케이스
solution = Solution()

# 테스트 1
test1 = "A man, a plan, a canal: Panama"
print(f"Expected: True")
print(f"Result: {solution.isPalindrome(test1)}")

# 테스트 2
test2 = "race a car"
print(f"Expected: False")
print(f"Result: {solution.isPalindrome(test2)}")

# 테스트 3
test3 = " "
print(f"Expected: True")
print(f"Result: {solution.isPalindrome(test3)}")


#시간 복잡도 : O(n), 입력 문자열 s의 모든 문자를 한 번씩 순회함(n = 입력 문자열의 길이)
    #for c in s 루프: O(n). 입력 문자열 s의 모든 문자를 한 번씩 순회하므로 O(n)
    #isalnum(), lower(), append()의 경우 : O(1), 각 문자에 대해 상수 시간이 걸림
    #'filtered == filtered[::-1]', '.join(filtered)'의 경우 : O(m) (m = 필터링된 문자열의 길이) 
    #m ≤ n, 최악의 경우 m = n

#공간 복잡도 분석: O(n), 모든 문자가 알파벳이나 숫자인 최악의 경우 m = n
    #filtered 리스트: O(m)
    #filtered[::-1]: O(m) 

class Solution:
    """
    1. 문자열을 반복문을 돌며 isdigit() or isalpha()이 True라면 string에 붙이기
    반복문이 끝나면 소문자로 모두 변경하고 뒤집은 문자와 같으면 True 반환
    시간 복잡도 (Time Complexity):
        - 문자열 순회: O(n)
        - 문자열 덧붙이기(string += i): O(n^2)  ← 파이썬에서 문자열은 불변이라 매번 새로운 문자열 생성
        - 소문자 변환 및 슬라이싱 비교: 각각 O(n)
        최종 시간 복잡도: O(n^2)

    공간 복잡도 (Space Complexity):
        - 필터링된 문자열 저장용 string: O(n)
        - 역순 문자열 생성: O(n)
        최종 공간 복잡도: O(n) 
    
    2. 문자열과 숫자인 것만 뽑아 리스트에 넣기
    시간 복잡도 (Time Complexity):
        - 리스트 컴프리헨션: O(n)
            - 각 문자에 대해 isalnum() → O(1), lower() → O(1) 이므로 전체 O(n)
        - 리스트 슬라이싱 및 비교(string == string[::-1]): O(n)
        총 시간 복잡도: O(n)

    공간 복잡도 (Space Complexity):
        - 리스트 string에 최대 n개의 문자 저장: O(n)
        - 슬라이싱된 string[::-1]도 새로운 리스트를 생성하므로 O(n)
        총 공간 복잡도: O(n)
    """
    def isPalindrome(self, s: str) -> bool:
        # string = ""
        
        # for i in s:
        #     if i.isdigit() or i.isalpha():
        #         string += i
        # string = string.lower()
        # return True if string == string[::-1] else False

        string = [i.lower() for i in s if i.isalnum()]
        return True if string == string[::-1] else False

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        string이 팰린드롬 문자열인지 판단하는 함수
        팰린드롬: 대소문자x 영문자&숫자 만으로 앞뒤가 동일한 문자열

        방법:
        1. 리스트를 필터/소문자화해서, 앞에서 반절과 뒤의 반절 (reverse)한 것을 비교하기
            -> 순회를 두번하게 됨
        2. 앞과 뒤에서 포인터 방식으로 찾기
            -> 영문자혹은 숫자가 아니면 건너뛰기
            -> isalnum으로 유효한 문자인지 판단
            -> 시간 복잡도 O(n) 공간 복잡도 O(1)
        Args:
            s (str): 검사할 문자열

        Returns:
            bool: 팰린드롬이면 True, 아니면 False
        """
        i, j = 0, len(s)-1
        answer = True
        while i < len(s) and j >= 0 and i < j:
            if s[i].isalnum() == False:
                i += 1
            elif s[j].isalnum() == False:
                j -= 1
            else:
                if s[i].lower() == s[j].lower():
                    answer = answer and True
                else:
                    answer = answer and False
                    break
                i += 1
                j -= 1
        return answer

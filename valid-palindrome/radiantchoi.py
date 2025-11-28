class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 선제적으로 소문자로 바꾼 문자열에서 알파벳이나 숫자인지를 걸러 낸다.
        s = list(filter(lambda x: x.isalnum(), s.lower()))
        
        # 처음과 끝에서 각각 한 칸씩 좁혀지는 인덱스의 구현을 위해 배열의 절반까지만 순회
        # 같은 위계에 있는 글자가 같지 않을 경우 early return
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1

        return True


"""
================================================================================
풀이 과정
================================================================================
- A man, a plan, a canal: Panama
- 띄어쓰기는 무시하고 앞 뒤에서 똑같은지 체크를 해야하네?
- 앞 포인터와 뒷 포인터에서 시작해서 띄어쓰기 만나면 건너뛰고
- 틀린것 나오면 False 반환하고, False를 만난적 없으면 True 반환

[1차 시도] Two Pointer
────────────────────────────────────────────────────────────────────────────────
1. 접근 방법
   - Two Pointer 사용: left는 앞에서, right는 뒤에서 시작
   - 유효하지 않은 문자(알파벳/숫자가 아닌 것)는 건너뛰기
   - 유효한 문자끼리 비교하며 중앙으로 이동

2. 구현
        left = 0
        right = len(s) - 1

        while left < right:
            # 왼쪽 포인터: 알파벳/숫자가 아니면 건너뛰기
            if not s[left].isalpha() and not s[left].isnumeric():
                left += 1
                continue

            # 오른쪽 포인터: 알파벳/숫자가 아니면 건너뛰기
            if not s[right].isalpha() and not s[right].isnumeric():
                right -= 1
                continue

            # 대소문자 무시하고 비교
            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1

        return True

4. 시간 복잡도: O(n) - 문자열을 한 번만 순회
5. 공간 복잡도: O(1) - 추가 공간 사용 없음 (포인터 2개만 사용)
"""

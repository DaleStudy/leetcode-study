class Solution:
    # Alphanumeric 스트링 이외의 문자열을 먼저 제외 시킨 이후 lowercase로 변경한 다음, 양 끝에서부터 문자열을 비교한다.
    def isPalindrome(self, s: str) -> bool:
        only_alnum_s = ''
        for ss in s:
            if ss.isalnum():
                # Alphanumeric이 맞다면 only_alnum_s에 문자열을 더한다.
                only_alnum_s += ss

        # only_alnum_s 내의 모든 문자를 lowercase로 변경한다.
        only_alnum_s = only_alnum_s.lower()

        for i in range(len(only_alnum_s) // 2):
            # string을 탐색할 index를 0부터 문자열의 반절까지 for문을 돌리며
            # 양 끝에서부터 i번 인덱스와 (len(only_alnum) - 1 - i)번 인덱스의 문자 값을 비교한다.
            # 같지 않은 경우에는 False로 early return해준다.
            if only_alnum_s[i] != only_alnum_s[len(only_alnum_s) - 1 - i]:
                return False

        return True

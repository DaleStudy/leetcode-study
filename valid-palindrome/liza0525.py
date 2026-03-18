# 문자열 길이가 n일 때
# 시간 복잡도: O(n)
# - alphanumeric 확인할 때 전체 문자를 순회하는 게 최대
# 공간 복잡도: O(n)
# - 최악의 경우는 입력 전체가 alphanumeric일 때(특수 문자 없을 때)

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


# 7기 풀이
# 시간 복잡도: O(n)
# - 문자열 s의 전체 문자를 순회할 때 길이 n만큼의 시간 소요
# 공간 복잡도: O(1)
# - start, end 등의 변수만 사용

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer로 각 문자열을 비교하며 palindrome인지 체크한다.
        # 해당 문제의 조건 중 하나가 alphanumeric한 문자만 체크하는 것
        start, end = 0, len(s) - 1

        # 양 끝의 포인터 인덱스가 같아지기 전까지 루프를 돌린다.
        while start < end:
            if not s[start].isalnum():
                # s[start] 문자가 alphanumeric하지 않은 경우엔 start 포인터를 오른쪽으로 한 칸 이동
                start += 1
                continue
            if not s[end].isalnum():
                # s[end] 문자가 alphanumeric하지 않은 경우엔 end 포인터를 왼쪽으로 한 칸 이동
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                # 두 문자의 lowercase가 동일하지 않은 경우에는 palindrome이 아니므로 False로 early return 해준다.
                return False
            start, end = start + 1, end - 1
        # while 루프가 다 돌았다면 조건에 걸리지 않고 palindrome임을 충족하므로 True를 return
        return True

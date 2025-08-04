# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        """
        [Complexity]
            - TC: O(m * k + n) (k = is_included() = len(set(t)))
            - SC: O(k) (res 제외)

        [Approach]
            다음과 같은 counter를 유지하며, two pointer로 window를 이동하며 min window substring을 트래킹한다.
                - 생성 시) t의 모든 문자에 대해 ++
                - pointer 이동 시) window에 포함되는 문자 중 t에 속하는 문자에 대해 --
        """
        from collections import Counter

        # early stop
        m, n = len(s), len(t)
        if m < n:
            return ""

        # t에 대한 counter 생성
        counter = Counter(t)

        # t의 모든 문자가 window에 포함되는지 확인하는 함수
        def is_included():
            # counter의 모든 값이 0 이하이면, t의 모든 문자가 window에 포함되는 것 (중복 포함)
            return all(c <= 0 for c in counter.values())

        lo, min_len = 0, 1e6
        res = ""

        for hi in range(m):
            # 현재 window에 포함된 문자를 counter에 반영
            if s[hi] in counter:
                counter[s[hi]] -= 1

            # t의 모든 문자가 window에 포함되어있다면(= counter의 모든 값이 <= 0이면),
            # counter 값이 음수 ~ 0이 될 때까지 lo 증가시키면서 (min window를 구해야하므로) counter 업데이트
            if is_included():
                while True:
                    # window의 첫 번째 문자가 t에 속하는 문자라면
                    if s[lo] in counter:
                        # counter에서의 값이 0이면, 더이상 lo를 오른쪽으로 줄일 수 없음
                        if counter[s[lo]] == 0:
                            break
                        # coutner에서의 값이 음수라면, lo를 오른쪽으로 줄일 수 있으므로 counter 반영
                        else:
                            counter[s[lo]] += 1
                    # lo를 오른쪽으로 한 칸 이동
                    lo += 1

            # (1) t의 모든 문자가 window에 포함되어 있고 (2) 현재 window의 length가 min_len 보다 작다면
            # window substring 업데이트
            if is_included() and (new_len := hi - lo + 1) < min_len:
                min_len = new_len
                res = s[lo:hi + 1]

        return res

    def minWindow(self, s: str, t: str) -> str:
        """
        [Complexity]
            - TC: O(m + n)
            - SC: O(k)

        [Approach]
            1) 위의 풀이에서 is_included()를 실행하는 데에 O(k)이 소요되므로,
               (t에 속하는 문자 중, 아직 window에 모두 포함되지 않은 문자 종류 개수)를 트래킹하는 변수 remains를 이용하여 최적화 한다.
               즉, remains == 0이라면 is_included()인 것과 동일하다.
            2) 반복문 안에서 문자열 슬라이싱으로 res를 업데이트 할 때 추가적인 복잡도가 소요된다.
               따라서 min window에 대한 pointer인 min_lo, min_hi만 트래킹하고, return 문에서 문자열 슬라이싱으로 반환한다.
               단, min window substring이 존재하지 않는다면 결과가 빈 문자열이 될 수 있으므로, min_lo ~ min_hi - 1 범위를 반환하도록 한다.
        """
        from collections import Counter

        # early stop
        m, n = len(s), len(t)
        if m < n:
            return ""

        # t에 대한 counter 생성
        counter = Counter(t)

        # counter의 값을 모두 확인하는 is_include() 최적화
        remains = len(counter)  # t에 속하는 문자 중, 아직 window에 모두 포함되지 않은 문자 종류 개수
        lo = min_lo = min_hi = 0
        min_len = m + 1

        for hi in range(m):
            # 현재 window에 포함된 문자를 counter에 반영
            if s[hi] in counter:
                counter[s[hi]] -= 1
                # 현재 window에 해당 문자가 t에 존재하는 개수만큼 들어와있다면, remains--
                if counter[s[hi]] == 0:
                    remains -= 1

            # t의 모든 문자가 window에 포함되어있는 동안 lo 이동
            while not remains:
                # 최소 길이 window substring 갱신
                if (new_len := hi - lo + 1) < min_len:
                    min_len, min_lo, min_hi = new_len, lo, hi + 1

                # lo 이동 전, counter 업데이트
                if s[lo] in counter:
                    counter[s[lo]] += 1
                    # counter의 값이 0 초과가 된다면, 더이상 window에 해당 문자가 모두 들어있지 않다는 것이므로 remains++
                    if counter[s[lo]] > 0:
                        remains += 1

                # lo를 오른쪽으로 한 칸 이동
                lo += 1

        return s[min_lo:min_hi]

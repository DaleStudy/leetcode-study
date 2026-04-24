# 7기 풀이
# 시간 복잡도: O(n ** 2)
# - for문으로 문자의 중심을 탐색 * while문으로 양쪽으로 뻗어나가며 문자열 탐색
# 공간 복잡도: O(1)
# - 변수 몇 개만 사용
class Solution:
    # 해당 문제의 기본 아이디어: 중심 확장법을 이용하여 펠린드롬 찾기
    def countSubstrings(self, s: str) -> int:
        res = 0

        # 펠린드롬의 길이가 짝수일 수도 홀수일 수도 있기 때문에
        # 2 * len(s)를 돌고 나눈 수 몫을 이용해서 중심을 먼저 잡는다
        for idx in range(2 * len(s) - 1):
            # 펠린드롬 길이가 짝수일 때는 left와 right의 값이 1 차이나지만
            # 홀수일 때는 left == right 이다. 
            left = idx // 2
            right = (idx + 1) // 2
            delta = 0

            while (
                0 <= left - delta  # 왼쪽으로 확장했을 때의 index와
                and right + delta < len(s)  # 오른쪽으로 확장했을 때의 index가 모두 s길이 범위 내에 있어야 함
            ):
                if s[left - delta] == s[right + delta]:  # 두 개가 같은 경우에는 펠린드롬
                    res += 1  # 결과 값을 하나 추가하고
                    delta += 1  # 확장을 위한 값을 1 올려준다
                else:
                    # 확장했을 때의 양 쪽 문자가 다른 경우에는 펠린드롬이 아니므로 break하고
                    # 다음 루프에서 새로운 중심을 잡은 후 다시 펠린드롬을 찾는다.
                    break

        return res

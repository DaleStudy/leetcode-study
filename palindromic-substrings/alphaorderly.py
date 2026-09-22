"""
시간복잡도 : O(N^2)
공간복잡도 : O(1)

1. n을 s의 길이로 설정한다.
2. count를 0으로 초기화한다.
3. 각 문자를 중심(center)으로 확장하여 홀수 길이의 팰린드롬을 센다.
   - radius를 0부터 시작해, center - radius >= 0, center + radius < n 이고 s[center - radius] == s[center + radius]인 동안 count를 1 증가, radius += 1 한다.
4. 각 문자 쌍(center, center+1)을 중심으로 확장하여 짝수 길이의 팰린드롬을 센다.
   - radius를 0부터 시작해, center - radius >= 0, center + radius + 1 < n 이고 s[center - radius] == s[center + radius + 1]인 동안 count를 1 증가, radius += 1 한다.
5. 총 팰린드롬 부분 문자열 개수인 count를 반환한다.
"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for center in range(n):
            radius = 0
            # 홀수 길이 팰린드롬 (center를 기준)
            while (
                center - radius >= 0
                and center + radius < n
                and s[center - radius] == s[center + radius]
            ):
                count += 1
                radius += 1

            radius = 0
            # 짝수 길이 팰린드롬 (center, center+1을 기준)
            while (
                center - radius >= 0
                and center + radius + 1 < n
                and s[center - radius] == s[center + radius + 1]
            ):
                count += 1
                radius += 1

        return count

"""
Constraints:
- 0 <= n <= 10^5

Time Complexity: O(n log n)
- 외부 루프: O(n) (0부터 n까지 반복)
- hammingWeight 함수: O(log n)
- 총 시간 복잡도: O(n) * O(log n) = O(n log n)

Space Complexity: O(n)
- 결과를 저장하기 위한 길이 n+1의 배열 필요

풀이방법:
1. 길이가 n+1인 ans 배열을 생성
2. 0부터 n까지의 각 숫자에 대해:
   - hammingWeight 함수를 사용하여 숫자 i를 이진수로 변환했을 때 1의 개수 계산
   - 결과를 ans[i]에 저장
3. ans 배열 반환
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)

        for i in range(n+1):
            ans[i] = self.hammingWeight(i)
        return ans

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

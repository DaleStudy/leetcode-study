'''
문제 풀이
- 이중 for 문으로 구현시 O(n^2) 으로 시간 초과
- least_num에 현재 날짜 이전에 가장 싸게 살 수 있는 금액을 업데이트
- dp로 해당 날짜까지 가장 큰 수익을 저장
시간 복잡도: O(n)
- for 문 하나 -> O(n)
공간 복잡도: O(n)
- dp 리스트 -> O(n)
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        least = prices[0]
        for i in range(len(prices)):
            least = min(prices[i], least)
            largest = max(prices[i] - least, largest)
        return largest
            

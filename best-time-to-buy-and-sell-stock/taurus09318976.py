'''
- 이 문제는 최저가에 한 주식을 사서, 그 이후에 최대가에 팔아야 하는 문제임
- 만약 이익을 낼 수 없으면 0을 반환함
조건 : 
1) 반드시 한 번만 사고 한 번만 팔아야 하며, 팔기 전에 반드시 사야 함
2) 팔 때는 구매한 날 이후의 날짜여야 합니다.

Example 1. 의 경우
날짜 (index)| 가격 (price) | min_price (최저가) | current_profit (현재 이익) | max_profit (최대 이익)
0            7              7(초기값)            -                         0(초기값)
1            1              7 -> 1              -                        0
2            5              1                  5 - 1 = 4                 0 -> 4
3            3              1                  3 - 1 = 2                 4
4            6              1                  6 - 1 = 5                 4 -> 5
5            4              1                  4 - 1 = 3                 5

'''
class Solution:
    def maxProfit(self, prices: List[int]):
        # 입력 배열이 비어 있으면 주가가 없으므로 거래할 수 없음. 따라서 최대 이익은 0
        if not prices:              
            return 0

        # 배열의 첫 번째 가격을 최저가로 초기화함. 이후 가격과 비교할 기준점이 됨
        min_price = prices[0]
        # 이익이 없으면 0을 반환하기 위해 최대 이익을 0으로 초기화함       
        max_profit = 0              

        for price in prices[1:]:    # 두 번째 가격부터 순회. 첫번째 가격은 이미 min_price에 할당했으므로 제외함.
            if price < min_price:   # 현재 가격이 최저가보다 작으면 갱신. 더 싸게 살 수 있는 날을 찾는 과정임
                min_price = price
            else:
                profit = price - min_price  # 현재 가격에서 최저가를 빼서, 지금 팔면 얻을 수 있는 이익 계산
                if profit > max_profit:     # 계산한 이익이 기존의 최대 이익보다 크면 max_profit 갱신
                    max_profit = profit

        return max_profit           # 반복이 끝나면 최대 이익을 반환


    '''
    시간 복잡도 : O(n)
        배열을 한 번만 순회하기 때문에 입력 크기 n에 비례함
        n은 prices 배열의 길이
    
    공간 복잡도 : O(1)
        추가로 사용하는 변수는 min_price, max_profit, profit 3개뿐임(상수 개수),
        입력 크기에 따라 달라지지 않음
        입력 배열 외에 별도의 저장 공간이 필요하지 않음
    '''
        

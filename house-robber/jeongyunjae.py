class Solution:
    def rob(self, nums: List[int]) -> int:
        result = list(nums)

        for i, data in enumerate(result):
            if i <= 1:
                continue
            
            stolen_money = result[i]
            before_house_money = result[i-1]

            for j in range(i-1):
                if result[i] + result[j] > stolen_money:
                    stolen_money = result[i] + result[j]

            result[i] = max(before_house_money, stolen_money)    

        return max(result)

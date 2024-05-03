'''
Brainstorm
- Brute force: double for-loop O(N^2)
- Efficient: single pass O(N)

Plan
1. Initialize the variables
2. Iterate through each price
    2-1. Update the min price
    2-2. Calculate and update max profit
3. Return the max profit
'''


def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

#TC: O(N), SC: O(1)

# Normal Case
print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)  
print(maxProfit([7, 6, 4, 3, 1]) == 0)  

# Edge Case
print(maxProfit([]) == 0)  
print(maxProfit([1]) == 0)  


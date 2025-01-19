        #해석
        #prices list를 순회하면서 최솟값 min_val을 업데이트 한다
        #현재 prices[n]과 min_val의 차를 업데이트 해준다. 


        #Big O
        #N: prices 의 크기
        
        #Time Complexity: O(N)
        #- for loop : prices의 원소 갯수만큼 순회하므로 O(N)

        
        #Space Complexity: O(1)
        #- min_val, answer : 변수는 상수이므로 O(1)
class Solution(object):
    def maxProfit(self, prices):

        #Initialize variables
        min_val = prices[0] 
        answer = 0

        for n in range(len(prices)):
            min_val= min(min_val,prices[n]) #Update min value of the prices list
            answer = max(prices[n]-min_val,answer) #Update max value of prices[n] - min value

        return answer
    

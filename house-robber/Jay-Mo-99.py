# --- 해석 ---
#매개변수 nums 를 순회하면서 nums[i] 일때의 최대 누적값을 업데이트 한다
#prev1은 현재까지의 최고 누적금액, prev2는 이전 집까지의 최고 누적금액이다. 
#현재 집 nums[i] 를 도둑질 하려면, 이전 집까지의 최고금액(prev2) + 현재 집(nums[i])이다.
#현재 집 nums[i]를 도둑질에 제외하려면 현재까지의 최고 금엑(prev1) 이다. 
#loop 당 저 둘의 최댓값을 선택하여 current변수에 update해준다. 
        
# --- Big O
#N: 매개변수 nums의 길이가 N이다. 
        
# Time Complexity: O(N)
#- for loop 는 nums[0] 부터 nums[len(nums)]만큼 순회: O(N)
        
# Space Complexity: O(1)
#-current,prev1,prev2 는 nums와 무관한 상수 메로리 할당: O(1)


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #prev1: 현재 집까지의 최고 금액
        #prev2: 이이전 집까지의 최고 금액 
        prev1,prev2=0,0

        for num in nums:
            #current는 prev1과 prev2+num 중 큰 값을 update
            current = max(prev1,prev2+num)
            prev2 = prev1 #current업데이트 이후 prev1(현재 최고금액) 이 prev2(이어진 집까지 최고금액)가된다
            prev1= current #prev1은 현 num까지 고려된 current의 값이다. (현재 최고 금액액)
        return prev1
nums = [2,7,9,3,1]
solution = Solution()
solution.rob(nums)


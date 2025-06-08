class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # 연속된 부분 배열의 곱이 가장 큰 값 찾기(정수)
        # DP (시간복잡도 O(n), 공간복잡도 O(1))
        answer = nums[0]
        prev_max = prev_min = nums[0]
        
        for i in range(1,len(nums)):
            n = nums[i]
            
            # 음수*음수는 양수이므로 max,min 둘다 계산
            curr_max = max(n,prev_max*n, prev_min*n)
            curr_min = min(n,prev_max*n, prev_min*n)

            answer = max(answer, curr_max)  # 최대 곱 업데이트
            prev_max, prev_min = curr_max, curr_min # 현재값을 이전값으로 업데이트

        return answer

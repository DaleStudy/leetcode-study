class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # 그리디(시간복잡도 O(n), 공간복잡도 O(1))
        max_reach = 0   # 가장 멀리 갈 수 있는 위치

        for i in range(len(nums)):
            # max_reach가 i보다 작으면 nums[i]에 도달 불가 -> False
            if i > max_reach:
                return False
            # 현재 위치i에서 점프했을 때 도달 가능한 최대 위치 업데이트
            max_reach = max(max_reach, i + nums[i])

        # 도달 가능
        return True

        
        # # 아래 방식(DP)은 시간초과뜸.
        # # DP(시간복잡도 O(n^2), 공간복잡도 O(n))
        # # dp[i] = i번째에 도달 가능한지 여부
        # dp = [False]*len(nums)  
        # dp[0] = True    # 시작점은 항상 도달 가능

        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         # j까지 갈 수 있고, j에서 i까지 점프 가능하면, True로 바꾸고 break(더 볼 필요없음)
        #         if dp[j] and j + nums[j] >= i:
        #             dp[i] = True
        #             break

        # # 마지막 인덱스 도달 여부
        # return dp[-1]

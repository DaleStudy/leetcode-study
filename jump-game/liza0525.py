# 7기 풀이
# 시간 복잡도: O(n)
# - nums의 길이(n) 만큼 시간 소요
# 공간 복잡도: O(1)
# - 변수(max_reach)만 사용
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 매 순간에 가장 멀리 갈 수 있는 index 저장

        for i in range(len(nums)):
            if i > max_reach:
                # 현재의 인덱스가 max_reach보다 크면, 도달 자체를 할 수 없음을 의미
                # 따라서 False로 early return
                return False

            # 기존의 max_reach와 i에서 최대로 갈 수 있는 거리를 계산한 값을 비교하여
            # 더 큰값으로 max_reach 업데이트
            max_reach = max(max_reach, i + nums[i])

        # for문을 모두 돌았다는 것은 맨 끝 인덱스에 도달 가능하다는 것을 의미
        # True로 리턴한다.
        return True

# 링크: https://leetcode.com/problems/two-sum/

# [요구사항]
# - 정수 배열 nums에서 두 숫자를 더했을 때 target이 되는 두 수의 "인덱스"를 반환한다.
# - 반환하는 배열의 순서는 아무렇게나
# - 같은 원소를 두 번 사용하면 안 된다.
#   - ex) nums: [3,3] / target: 6 일 때 [0, 1]은 정답, [0, 0]은 오답
# - 단 하나의 해만 존재함

# [접근법]
# 1. hashMap을 선언
# 2. 배열을 순회하며 숫자를 hashMap에 담는다
    # 3. 현재 숫자와 합쳐서 target이 되는 숫자가 hashMap에 있는지 탐색
    # 4. step3을 만족하는 숫자가 있으면 즉시 반환, 아니면 hashMap에 저장

# [복잡도] 
# - Time: O(N), for문 순회하는 비용
# - Space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} # Space: O(N)

        for i, num in enumerate(nums): # Time: O(N)
            pair = target - num # 쌍을 만족하는 숫자 추출
            if pair in num_map: # 쌍을 만족하는 숫자가 이미 존재하면 즉시 종료
                return [i, num_map[pair]]
            num_map[num] = i 

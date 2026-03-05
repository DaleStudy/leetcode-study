# 시간 복잡도: O(n)
# - for문 하나로 linear 탐색
# 공간 복잡도: O(n)
# - check_set은 최대 n개만큼 늘어날 수 있음
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_set = set()
        for num in nums:
            if num in check_set:
                # check_set에 이미 있는 경우라면 중복 숫자가 있으므로 True를 return
                return True
            # check한 숫자는 set에 저장
            check_set.add(num)
        # for문 모두를 돌았다면 중복 숫자가 없다는 의미이므로 False를 return
        return False

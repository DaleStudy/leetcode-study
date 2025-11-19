# 문제 내용
# 배열 nums에 같은 값이 2번 이상 등장하면 True, 아니면 False.
# 가장 실전적인 방법: 해시셋(Set)으로 한 번씩 보며 등장 여부 체크
# → 이미 본 값이면 바로 True 반환(조기 종료).

#  문제 풀이 설명
# set은 중복을 허용하지 않는 집합이다
# 리스트르 set으로 바꾸면 중복이 제거된다
# 따라서 길이를 비교하면 중복 여부를 알 수 있다

# 중복이 있는 경우
# >>> nums = [1,2,3,2]
# >>> len(nums)
# 4
# >>> set(nums)
# {1, 2, 3}
# >>> len(set(nums))
# 3
# >>> len(nums) != len(set(nums))
# True

# 중복이 없는 경우
# >>> nums = [1,2,3]
# >>> len(nums)
# 3
# >>> set(nums)
# {1, 2, 3}
# >>> len(set(nums))
# 3
# >>> len(nums) != len(set(nums))
# False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


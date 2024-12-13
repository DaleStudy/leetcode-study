

'''
풀이:
    중복된 요소가 있는지 찾는 문제입니다.

    hash set 으로 중복을 제거하고
    기존 nums 의 길이와 중복 제거된 nums_set 의 길이가 같은지 return 했습니다.

시간 복잡도:
    O(n) - has set 을 만드는 시간

공간 복잡도:
    O(n) - n개의 요소를 set에 담기 때문
'''


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        return len(nums_set) != len(nums)

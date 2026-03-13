class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        nums를 set으로 바꿨을 때 길이가 줄어들면 배열 안에 중복 값이 있다는 의미입니다.
        """
        if len(nums) != len(set(nums)):
            return True
        else:
            return False


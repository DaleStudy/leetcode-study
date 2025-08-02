class Solution:
    # 리스트 안에 동일한 숫자가 2개 이상 존재하면 true를 반환해야 하는 문제
    # Set으로 변환 시 중복이 제거되므로 List와 Set의 크기를 비교해 답을 구할 수 있음
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # Time Complexity
    # - set(nums) → O(n)
    # - len(nums), len(set(nums)) → O(1)
    # - Total: O(n) (n = number of list elements)


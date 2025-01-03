class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition:
            기존에 풀었던 3sum 문제와 유사하게,
            해시에 현재 숫자와 더해서 target이 되는 값을 찾는다.
            만약 없을 경우, 해시에 현재 값과 인덱스를 저장한다.

        Time Complexity:
            O(N):
                해시는 접근하는 데에 O(1)이 소요되고,
                총 N번 반복해야 하므로 시간복잡도는 O(N)이다.

        Space Complexity:
            O(N):
                최악의 경우 해시에 N개의 숫자와 인덱스를 저장해야 한다.
        """
        complement_dict = {}
        for i, num in enumerate(nums):
            if target - num in complement_dict:
                return [complement_dict[target - num], i]
            else:
                complement_dict[num] = i

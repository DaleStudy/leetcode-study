class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        리스트에서 두 숫자의 합이 target이 되는 경우가 있으면, 그 두 숫자의 인덱스를 반환하는 함수

        방법:
        1. 리스트를 순회하면서, 각 숫자에서 target을 만들기 위한 나머지 숫자가 있는지 모두 순회 (brute-force); o(n^2) 시간복잡도
        2. 리스트를 순회하면서, 각 숫자에서 target을 만들기 위한 나머지 숫자가 있는지 search (binary search); o(nlogn) 시간복잡도
        3. 리스트를 순회하면서, 각 숫자를 dict에 저장하여 (key=숫자, value=인덱스), 
        target을 만들기 위한 나머지 숫자를 dict에서 search; o(n) 시간복잡도 -> PICK!
        
        * 답이 항상 존재한다는 가정하에 문제를 풀이.
        * 리스트의 길이가 2 이하인 경우, 두 숫자의 합이 target이 되는 경우가 항상 존재하므로 [0, 1]을 반환한다.

        Args:
            nums (list[int]): 중복을 포함한 정수 배열
            target (int): 찾아야 하는 두 숫자의 합

        Returns:
            list[int]: 찾아낸 두 숫자의 인덱스
        """
        if len(nums) <= 2:
            return [0, 1]
        seen = dict()
        for i, num in enumerate(nums):
            remain = target - num
            if remain in seen:
                return [seen[remain], i]
            seen[num] = i

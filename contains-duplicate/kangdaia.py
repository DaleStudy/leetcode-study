class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        리스트에 숫자가 두번 이상 등장하는 경우가 있으면 True, 
        모든 숫자가 한 번씩만 등장하면 (unique) False를 반환하는 함수
        
        방법:
        1. 처음부터 끝까지 리스트를 순회하면서 동일한 숫자가 있는지 확인하는 방법 (with dict); o(n) 시간복잡도
        2. 리스트를 set으로 변환하여 길이를 비교하는 방법; o(n) 시간복잡도 -> PICK!
        3. 리스트를 정렬한 후 인접한 숫자가 동일한지 확인하는 방법; o(nlogn) 시간복잡도
        
        * 길이가 1일 경우, 중복이 있을 수 없으므로 False를 반환한다.
        
        방법(2)가 가장 간단하고 효율적이지만, 메모리 사용량은 길이가 n인 리스트를 set으로 변환할 때 O(n) 만큼 필요하다.
        방법(3)은 추가적인 메모리를 사용하지 않지만, 정렬할 때 O(nlogn) 시간복잡도가 든다.

        Args:
            nums (List[int]): 동일한 숫자를 포함한 정수 배열

        Returns:
            bool: 중복이 없으면 False, 있으면 True
        """
        if len(nums) <= 1:
            return False
        return len(nums) != len(set(nums))
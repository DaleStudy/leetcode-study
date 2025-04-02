class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        nums 리스트에 중복 값이 나오면 false,
        리스트에 중복 값이 없으면 true를 반환한다.
        - Time Complexity: O(n)
            * 전체 배열을 한 번씩 순회하면서 중복 여부를 확인한다.
        - Space Complexity: O(n)
            * Python에서 set()은 배열의 각 원소를 해시 테이블에 저장한다.
            배열에 중복된 요소가 전혀 없다면 모든 요소(n개)를 set에 저장하게 되므로
            공간 복잡도는 O(n)이 된다.
        """
        seen = set() # 중복 여부 확인하는 set 객체
        for item in nums:
            if item in seen:
                return True
            seen.add(item)
        return False 
      
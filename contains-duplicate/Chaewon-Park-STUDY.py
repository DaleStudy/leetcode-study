class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        store = set()
        # count를 쓰면 매번 전체 배열을 훑어 O(n^2) → Time out
        # 대신 해시 기반 set을 쓰면 in 확인이 평균 O(1)이라 전체 O(n)
        # Time: O(n), Space: O(n)
        for elem in nums:
            if elem in store:
                return True
            else:
                store.add(elem)
        return False
        

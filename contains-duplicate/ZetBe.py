'''
문제: 배열의 중복을 찾는 문제 
풀이: 정렬 후 인접한 원소끼리 비교하여 중복 여부 확인 중복이 없다면 False 반환

시간복잡도: O(n log n)
sort()의 시간복잡도는 O(n log n)이고, for문은 O(n)이므로, 
전체 시간복잡도는 O(n log n)

공간복잡도: O(1)
nums.sort()는 제자리 정렬이므로, 추가적인 공간을 사용하지 않는다.
또한 num 변수를 하나만 사용하므로, 전체 공간복잡도는 O(1)

사용한 자료구조: 리스트

만약 파이썬의 딕테이션과 같이 조회 시 O(1)인 자료구조를 사용한다면, 
시간복잡도를 O(n)으로 줄일 수 있다.
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num = nums[0]
        for i in range(1, len(nums)):
            if num == nums[i]:
                return True
            num = nums[i]
        return False
        


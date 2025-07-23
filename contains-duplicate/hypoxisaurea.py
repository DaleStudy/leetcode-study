
'''
풀이:
    배열 nums 에 중복된 값이 있는지 효율적으로 검사하기 위해 해시 집합(Hash Set) 사용

    빈 집합 num_set
    배열의 각 요소 num을 순회하며:
    만약 num이 이미 num_set에 들어있다면 → 중복이므로 즉시 True 반환
    아니라면 num_set에 num을 추가하고 다음 요소로 넘어감
    순회를 모두 마쳤음에도 중복을 발견하지 못했다면 False 반환

시간 복잡도: O(n)
    배열을 한 번 순회하며, 각 요소마다 집합에 대한 조회(in)와 삽입(add) 연산 수행
    파이썬 set의 평균 조회·삽입 비용은 O(1)이므로 전체 O(n)

공간 복잡도: O(n)
    최악의 경우 배열의 모든 요소가 중복 없이 집합에 저장되므로, 추가로 n개의 공간을 사용
'''


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)

        return False
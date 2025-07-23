'''
1. Brute Force 풀이:
    배열의 각 위치 i를 기준으로 diff = target - nums[i] 를 계산하고
    그 뒤쪽(i+1부터 끝까지) 요소들 중 nums[j] == diff 인 j를 찾으면
    [i, j] 반환

시간 복잡도: O(n²)
    이중 루프를 돌며 모든 쌍을 검사

공간 복잡도: O(1)
    추가 자료구조를 사용하지 않고 상수 공간만 소모

    
2. Hash Map 풀이:
    빈 딕셔너리 lookup = {} 준비
    배열을 순회하며 각 요소 num에 대해 diff = target - num 을 계산

    if diff in lookup:
        보수가 이미 맵에 있으면 즉시 [lookup[diff], i] 반환
        그렇지 않으면 lookup[num] = i 로 현재 값과 인덱스를 기록
    순회 종료 후에도 못 찾으면 에러 발생

시간 복잡도: O(n)
한 번 순회하며 딕셔너리 조회·삽입이 평균 O(1)

공간 복잡도: O(n)
최악의 경우 모든 요소를 맵에 저장
'''


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]

            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i, j]

        raise ValueError('No answer')


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in lookup:
                return [lookup[diff], i]
                
            lookup[num] = i

        raise ValueError('No answer')
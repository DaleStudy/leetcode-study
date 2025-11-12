'''
Approach:
    주어진 배열을 두 번 순회하며 모든 가능한 쌍을 검사합니다.
    각 원소에 대해 이후의 원소들과의 합이 target과 같은지 비교하여 일치하는 경우 인덱스를 반환합니다.

Time Complexity:
    O(n²)
    - Outer Loop에서 n번 반복
    - Inner Loop에서 각 idx마다 최소 n-1번 반복

Space Complexity:
    O(1)
    - 결과를 저장하기 위해 상수 값을 필요로 하지만, 입력값의 크키에 비례한 새로운 공간 불요
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, xnum in enumerate(nums):
            for jdx in range(idx + 1, len(nums)):
                if (xnum + nums[jdx]) == target:
                    return [idx, jdx]
        return []
                
'''
(개선)
Approach:
    “You may assume that each input would have exactly one solution, and you may not use the same element twice.”
    라는 문구에서 항상 정답이 존재하며 같은 원소를 중복 사용할 수 없음을 알 수 있습니다. 
    이를 바탕으로 각 원소 num에 대해 (target - num)이 이전에 등장한 적이 있는지를 해시맵을 이용해 빠르게 확인하도록 개선했습니다.
    즉, 중복이 없고 답이 반드시 존재한다는 조건 아래에서, inner loop 없이 바로 찾기 위해 딕셔너리를 사용하 것입니다.

Time Complexity:
    O(n)
    - 리스트를 한 번 순회하면서 딕셔너리를 채워 넣는 데 걸리는 전체 시간

Space Complexity:
    O(n)
    - 해시맵에 key-value 쌍으로 저장되는 공간
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[num] = i

        
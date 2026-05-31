from typing import List


class Solution:
    """
    풀이:
    - 배열을 한 번 순회하면서, 각 숫자에 대해
      "나와 더해서 target이 되는 짝(complement)"이
      이미 등장했는지를 dict로 확인한다.
    - dict에 {숫자: 인덱스}를 저장해두면, complement 조회가 O(1)이므로 전체 O(n).
    - complement를 먼저 확인하고, 그 다음에 현재 숫자를
      dict에 넣기 때문에 같은 값이 두 번 나오는 경우
      (예: [3,3], target=6)에도 정상 동작한다.

    TC: O(n)
      - for 루프: nums의 모든 원소를 최대 한 번 순회. O(n)
        - complement 계산 (target - num): O(1)
        - dict에서 complement 존재 여부 확인 (in 연산): 해시 기반이라 평균 O(1)
        - dict에 현재 숫자 삽입: 평균 O(1)
      - 최악의 경우(답이 마지막 쌍): n번 반복. 최선의 경우(답이 첫 두 원소): 2번 반복

    SC: O(n)
      - nummap(dict): 최악의 경우 n-1개의 원소를 저장 (마지막 원소 직전까지 다 넣음). O(n)
      - complement, i, num: 입력 크기와 무관한 상수. O(1)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = dict()

        for i, num in enumerate(nums):
            complement = target - num

            if complement in nummap:
                return [nummap[complement], i]

            nummap[num] = i

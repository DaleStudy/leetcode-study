from typing import List

"""
문제 설명:
정렬되지 않은 정수 배열에서 가장 긴 연속된 숫자 수열의 길이를 반환하는 문제
O(n) 시간복잡도로 해결해야 함 => 정렬 x

목표:
- 해시 세트로 중복 제거
- 연속 수열의 시작점 찾기

[100,4,200,1,3,2]
- 해시 세트: {100, 4, 200, 1, 3, 2}
- 시작점 찾기: 1 (0이 없음), 100 (99가 없음), 200 (199가 없음)
- 1에서 시작: 1→2→3→4 (길이 4)
- 100에서 시작: 100만 (길이 1)
- 200에서 시작: 200만 (길이 1)
- 최대 길이: 4

- for num=1: 0이 없으므로 시작점 → while에서 1,2,3,4 처리
- for num=2: 1이 있으므로 while 스킵
- for num=3: 2가 있으므로 while 스킵
- for num=4: 3이 있으므로 while 스킵
→ 각 숫자가 while에서 1번만
"""

"""
시간복잡도: O(n)
- set(nums) 변환: O(n)
- 외부 for 루프: O(n)번 실행
- while 총 실행 횟수: 전체 알고리즘에서 각 숫자가 while 안에서 최대 1번만 처리됨
 → 총 while 내부 작업 = n번 → O(n)
- 해시 조회: O(1) × 총 조회 횟수
- 전체: O(n) + O(n) + O(n) = O(n)

공간복잡도: O(n)
- num_set: 최대 n개의 서로 다른 숫자 저장 -> O(n)
- 기타 변수들: O(1)
- 전체: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0


        for num in num_set:

            # 루프 안에서 한번만 처리
            if num - 1 not in num_set:
                current_length = 1

                while num + current_length in num_set:
                    current_length += 1

                max_length = max(max_length, current_length)


        return max_length

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))


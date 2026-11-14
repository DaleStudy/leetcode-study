"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

시간 복잡도: O(n)
- set 생성 O(n)
- 각 고유 숫자의 시작점 여부 확인 O(n)
- 연속 수열 탐색 O(n)

공간 복잡도: O(n)
- 모든 숫자를 set에 저장

풀이 : 
- 시간 복잡도 O(n)를 만족시키기 위해 set으로 연속되는 다음 숫자의 존재 여부만 확인
- 이전 숫자가 있는지 확인 후 시작점에서만 순회하여 중복 탐색 방지
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        answer = 0

        for num in num_set:
            # 시작점인지 확인
            if num - 1 not in num_set:
                current = num
                length = 1

                # 연속 숫자 탐색
                while current + 1 in num_set:
                    current += 1
                    length += 1
            
                answer = max(answer, length)
        
        return answer



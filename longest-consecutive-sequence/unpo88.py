class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            # 조기 종료: 남은 숫자보다 max_length가 크면 더 이상 불가능
            if max_length >= len(nums_set):
                break
                
            # 수열의 시작점인지 확인 (이전 값이 없어야 함)
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1
                
                # 연속된 다음 숫자들을 찾아가며 길이 계산
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length

""" 
================================================================================
풀이 과정
================================================================================

[문제 분석] 연속 수열의 최대 길이 찾기
────────────────────────────────────────────────────────────────────────────────
1. 연속 수열의 길이를 반환해야하는데
2. O(n) 시간 내에 동작하는 알고리즘으로 만들어야하네
   → 시간을 획기적으로 줄여야하니까 set을 사용하면 좋으려나?


[구현 전략] 기준점 기반 탐색
────────────────────────────────────────────────────────────────────────────────
3. 연속 수열이니까 특정 기준점으로부터 + 1인 값이 얼마나 반복되는지 최대 길이를 구해야겠다.
4. 특정 기준점이 여러 번 바뀔 수도 있는데, set으로 중복 제거를 했으니까 문제 없어보인다.
5. 기준점을 수열의 숫자가 시작하는 시점으로 잡으려면, 수열의 이전 값이 존재하지 않아야겠네

        nums_set = set(nums)
        max_length = 0

        for num in nums_set:
            if num - 1 not in nums_set:  # 수열의 시작점인 경우만
                current = num
                length = 1
            
                while current + 1 in nums_set:
                    current += 1
                    length += 1
            
                max_length = max(max_length, length)
        
        return max_length

6. 더 개선할 부분이 있나?
7. Claude에게 코드로 질문
8. Early Return 조건을 활용하라고 답변 (배열이 없는 경우와 남은 숫자보다 max_length가 더 큰 경우)

def longestConsecutive(self, nums: list[int]) -> int:
    if not nums:
        return 0
    
    nums_set = set(nums)
    max_length = 0

    for num in nums_set:
        # 조기 종료: 남은 숫자보다 max_length가 크면 더 이상 불가능
        if max_length >= len(nums_set):
            break
            
        if num - 1 not in nums_set:
            current_num = num
            current_length = 1
            
            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length
"""

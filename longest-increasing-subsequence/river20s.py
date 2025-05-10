# import bisect
from typing import List
class Solution():
    def _my_bisect_left(self, a: List[int], x:int) -> int:
        """
        정렬된 리스트 a에 x를 삽입할 가장 왼쪽 인덱스 반환
        """
        # x보다 크거나 같은 첫 번째 원소의 인덱스 찾아주기
        # bisect.bisect_left(a, x)를 직접 구현
        low = 0 # 시작 인덱스, 0으로 초기화
        high = len(a) # 끝 인덱스, 리스트의 길이로 초기화

        while low < high:
            mid = low + (high - low) // 2
            if a[mid] < x:
                low = mid + 1
            else: # a[mid] >= x
                high = mid
        return low # low가 삽입 지점

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        """
        if not nums: # nums가 빈 배열이라면 먼저 0 반환
            return 0
        tails = [] # 각 길이의 LIS를 만들 수 있는 가장 작은 마지막 값을 저장할 리스트
        for num in nums:
            # num을 삽입할 수 있는 가장 왼쪽 위치 찾기
            # -> tails 리스트에서 num 보다 크거나 같은 첫 번째 요소 인덱스 찾기
            # -> 만약 tails 모든 값보다 크다면 추가할 위치를 반환함
            idx = self._my_bisect_left(tails, num)

            # 만약 idx가 tails 현재 길이와 같다면
            # -> num이 tails의 모든 요소보다 크다
            # -> tails에 num "추가"
            if idx == len(tails):
                tails.append(num)
            # 만약 idx가 tails 현재 길이보다 작다면
            # -> 가능성 발견, tails[idx]를 num으로 "교체"
            # -> LIS를 개선
            else:
                tails[idx] = num

            # 모든 숫자 처리 후, tails 길이가 LIS길이가 됨
        return len(tails)


    """
    def lengthOfLIS_bruteforce(self, nums: List[int]) -> int:
        # 초기에 구현한 탐욕 기반 알고리즘
        # --- 복잡도 ---
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)
        # --- 한계 ---
        # [지금 당장 가장 좋아보이는 선택이 전체적으로는 최적이 아닌 경우]        
        # nums = [0,1,0,3,2,3] 같은 경우 답을 찾지 못함 (예측 값: 4, 실제 값: 3)
        # 각 요소에서 시작하여 탐욕적으로 다음 큰 수를 찾아가는 알고리즘으로 모든 LIS를 찾을 수 없음
        # 각 시작점에서 하나의 증가 부분 수열을 찾는 것, 항상 긴 것을 보장할 수 없음
        # 이미 찾은 LIS 뒤에 더 긴 LIS가 있다면 찾을 수 없음
        n = len(nums) # n은 nums의 길이(개수)
        if n == 0:    # 길이가 0이면 우선적으로 0을 반환
            return 0
        
        max_overall_length = 0 # 전체 최대 길이, 0으로 초기화

        for idx_i in range(n): # 0부터 n까지 순회하는 외부 루프
            current_length = 1 # 현재(index: idx_i) 부분 수열의 길이를 1로 초기화
            last_element_in_subsequence = nums[idx_i] # 부분 수열의 마지막 숫자를 현재 숫자로 초기화

            for idx_j in range(idx_i + 1, n): # 다음 요소의 인덱스를 idx_j로 하여 끝까지 순회
                # 만약 다음 요소가 부분 수열의 마지막 숫자보다 크다면
                if nums[idx_j] > last_element_in_subsequence:
                    # 마지막 숫자를 다음 요소로 갱신
                    last_element_in_subsequence = nums[idx_j]
                    # 현재 부분 수열의 길이를 1 증가
                    current_length += 1

            # 현재 부분 수열 길이가 전체 부분 수열 길이보다 큰 경우 갱신
            max_overall_length = max(max_overall_length, current_length)

        return max_overall_length
        """

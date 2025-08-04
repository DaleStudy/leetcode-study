'''
문제의 의도
이 문제는 배열에서 연속된 부분 배열의 곱이 최대가 되는 값을 찾는 문제임. 
음수가 있기 때문에 단순히 최대값만 추적하면 안 되고, 동시에 최소값도 추적해야 함.

핵심 포인트
음수 × 음수 = 양수 (큰 양수가 될 수 있음)
음수 × 양수 = 음수 (작아짐)
0이 있으면 곱이 0이 됨

해결 방법
동적 프로그래밍을 사용하되, 최대값과 최소값을 동시에 추적:

최대값: 양수 결과를 위해
최소값: 음수가 나중에 양수로 바뀔 가능성을 위해

시간 복잡도: O(n)
배열을 한 번만 순회하므로 O(n)
각 원소에서 상수 시간의 연산만 수행

공간 복잡도: O(1)
추가 배열을 사용하지 않음
몇 개의 변수만 사용하므로 상수 공간
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 빈 배열 처리
        if not nums:
            return 0
        
        # 첫 번째 원소로 모든 값들을 초기화
        max_product = nums[0]    # 전체 최대값
        current_max = nums[0]    # 현재 위치까지의 최대 곱
        current_min = nums[0]    # 현재 위치까지의 최소 곱
        
        # 두 번째 원소부터 배열을 순회하며 현재 숫자를 저장
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 현재 숫자가 음수일 경우를 대비해 max와 min을 임시 저장
            temp_max = current_max
            
            # 새로운 최대값 계산: 최대값과 최소값 모두 아래의 3개 중에서 나올 수 있음
            # num : 현재 숫자부터 새로 시작
            # temp_max * num : 현재숫자 × 이전최대값
            # current_min * num : 현재숫자 × 이전최소값(음수*음수=양수 가능성 떄문에)
            current_max = max(num, temp_max * num, current_min * num)
            
            # 새로운 최소값 계산: 나중에 음수와 곱해져서 큰 양수가 될 가능성을 위해
            # 현재 숫자, 현재숫자×이전최대, 현재숫자×이전최소 중 최소
            current_min = min(num, temp_max * num, current_min * num)
            
            # 지금까지의 전체 최대값과 현재 최대값을 비교하여 업데이트
            max_product = max(max_product, current_max)
        
        return max_product

        

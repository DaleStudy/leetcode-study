class Solution:
    #findMin 메서드는 정수 리스트를 입력 받아 정수를 반환
    def findMin(self, nums: List[int]) -> int:
        # 배열의 시작과 끝 인덱스 설정
        ## left는 배열의 시작 인덱스, right는 배열의 끝 인덱스. len(nums) - 1
        left, right = 0, len(nums) - 1
        
        #완전히 정렬되어 배열이 회전되지 않은 경우, 첫 번째 요소가 최소값
        if nums[left] < nums[right]:
            return nums[left]
        
        # 이진 탐색 실행 : left < right인 동안 반복되며, 검색 범위가 1개 이상의 요소를 포함할 때까지 계속됨
        while left < right:
            # 중간 인덱스 계산 : 중간값과 오른쪽 끝값 비교 후, 비교 결과에 따라 검색 범위 조정
            mid = (left + right) // 2
            
            # 중간값이 오른쪽 값보다 큰 경우
            # -> 최소값은 중간값 오른쪽에 있음
            if nums[mid] > nums[right]:
                left = mid + 1
            # 중간값이 오른쪽 값보다 작거나 같은 경우
            # -> 최소값은 중간값 포함 왼쪽에 있음
            else:
                right = mid
        
        # 최종적으로 찾은 최소값 반환
        return nums[left]

# 테스트 코드
print(Solution().findMin([3, 4, 5, 1, 2]))  # 출력: 1
print(Solution().findMin([4, 5, 6, 7, 0, 1, 2]))  # 출력: 0
print(Solution().findMin([1]))  # 출력: 1


    #시간 복잡도 (Time Complexity): O(log n)
        #이유:
            #이진 탐색 알고리즘 사용
            #각 단계마다 검색 범위가 절반으로 줄어듦
            #n개의 요소를 log₂n 번의 비교로 검색
            #예시:
            #n = 8: 최대 3번의 비교 (log₂8 = 3)
            #n = 16: 최대 4번의 비교 (log₂16 = 4)
            #따라서 시간 복잡도는 O(log n)
    #공간 복잡도 (Space Complexity): O(1)
        #이유:
            #추가적인 데이터 구조 사용하지 않음
            #사용하는 변수:
            #left, right, mid: 상수 개수의 정수 변수
            #입력 크기와 관계없이 일정한 메모리만 사용
            #따라서 공간 복잡도는 O(1)





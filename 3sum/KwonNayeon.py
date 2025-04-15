"""
Constraints:
1. 3 <= nums.length <= 3000
2. -10^5 <= nums[i] <= 10^5

Time Complexity: O(n^2)
- 정렬은 O(n log n), 이중 반복문은 O(n^2)
Space Complexity: O(n)
- 결과 리스트를 저장하는 데 필요한 공간

풀이 방법:
- 투 포인터를 활용하여 합이 0이 되는 세 수 조합 찾기
- 배열 정렬: 투 포인터 사용 + 중복 처리 용이
- for 루프: 첫 번째 숫자 선택 (len(nums)-2까지)
  - 중복된 첫 번째 숫자 건너뛰기
  - left, right 포인터 설정
- while 루프: 두 포인터가 교차하지 않아야 함
  - sum = nums[i] + nums[left] + nums[right] 계산
  - sum == 0: 결과 추가, 중복 건너뛰기, 양쪽 포인터 이동
  - sum < 0: left 증가 (더 큰 값 필요)
  - sum > 0: right 감소 (더 작은 값 필요)
- 최종 결과 반환
"""
# Brute-force: three nested loops → O(n^3)
# Optimized: sort + two pointer → O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        # Step 2: Fix one number using for loop
        # Step 3: Use two pointers to find two other numbers
        #   - if sum == 0: valid triplet
        #   - if sum < 0: move left pointer
        #   - if sum > 0: move right pointer
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1

                    left += 1
                    right -= 1
                
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
    
        return result

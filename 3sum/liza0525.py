class Solution:
    # 해당 문제는 two point 알고리즘을 사용한다. 이 때 '정렬'을 해야 알고리즘을 정확하게 적용할 수 있다.
    # 기준 값을 하나 정한 후, 그 값의 다음 인덱스부터 양 끝에 포인터를 두고 세 수의 합을 확인한다.
    # 만약 수가 0보다 작으면, 더 큰 수를 더해야 하므로 작은 값 쪽 인덱스를 하나 올리고
    # 0보다 크면, 더 작은 수를 더해야 하므로 큰 쪽 값의 인덱스를 낮춘다.
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums를 정렬한 후
        nums.sort()
        results = set()

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                # 정렬을 한 후의 가장 작은 수(i가 0일 때의 value)가 0보다 크다면,
                # 리스트 내 모든 수가 0보다 크기 때문에 합이 0이 될 수 없으므로 만족하는 답이 없으니 break 
                break

            if i > 0 and nums[i] == nums[i - 1]:
                # 이전 인덱스의 값과 동일한 값이라면 동일한 계산을 반복한 것이므로
                # 중복 계산을 피하기 위해 넘어간다.
                continue
            
            # i 인덱스를 기준으로 오른쪽으로 포인터 설정
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    # 합이 0보다 작으면 왼쪽 인덱스를 올린다
                    left += 1
                elif result > 0:
                    # 합이 0보다 크면 오른쪽 인덱스를 내린다
                    right -= 1
                else:  # result == 0
                    # 합이 0이면 답이 되므로 results에 추가하고
                    # 포인터들을 조정한다.
                    results.add((nums[i], nums[left], nums[right]))
                    left, right = left + 1, right - 1
        return list(results)


# 7기 풀이
# 시간 복잡도: O(n^2)
#  - 배열 정렬: O(n log n)
#  - for문과 while문을 이용한 이중 loop문으로 탐색: O(n^2)
#  - 전체 시간 복잡도는 O(n^2)
# 공간 복잡도: O(1)
#  - 결과 저장 공간은 output이므로 제외 (변수 이름: results)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 정렬을 한 번 한 후
        results = set()

        # for 문과 투포인터를 이용해 문제를 푼다.
        for i in range(len(nums) - 2):
            # i번째와 i - 1 번째 값이 같은 경우에는 이미 이전 loop에서 계산했기 때문에 다음 루프로 넘긴다
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 포인터 지정
            left, right = i + 1, len(nums) - 1
            while left < right:
                result = nums[i] + nums[left] + nums[right]
                if result < 0:
                    # 합이 0보다 작다면 요소의 값을 올려야 하기 때문에 left를 올린다. (nums는 정렬이 된 상태)
                    left += 1
                elif result > 0:
                    # 합이 0보다 크다면 요소의 값을 줄여야 하기 때문에 right를 내린다. (nums는 정렬이 된 상태)
                    right -= 1
                else:
                    # 합이 0이면 결과 저장 후, 포인터를 조정하여 다음 triplet 세트를 찾는다.
                    results.add((nums[i], nums[left], nums[right]))
                    left, right = left + 1, right - 1

        return list(results)

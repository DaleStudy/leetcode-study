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

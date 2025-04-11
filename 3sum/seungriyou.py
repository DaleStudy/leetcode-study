# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum_slower(self, nums: List[int]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(n)

        [Approach]
            two sum 문제에서 고정된 하나의 값만 추가해서 풀 수 있다.
            정렬을 한 차례하면, duplicated triplet 처리가 가능하다.
        """

        n = len(nums)
        nums.sort()

        def two_sum(fixed_idx):
            remains = {}
            fixed_val = nums[fixed_idx]
            res = set()

            for i in range(fixed_idx + 1, n):
                num = nums[i]
                if num in remains:
                    res.add((nums[fixed_idx], nums[remains[num]], nums[i]))
                remains[-fixed_val - nums[i]] = i

            return res

        res = set()
        for i in range(n - 2):
            if ts := two_sum(i):
                res |= set(ts)

        return [list(r) for r in res]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [Complexity]
            - TC: O(n^2)
            - SC: O(1) (res 제외한 extra space)

        [Approach]
            정렬 후, 하나의 값을 고정해두고 two pointer를 사용하는 방식을 적용할 수 있다.
            이때 매 turn에서 중복 원소를 고려해서 미리 이동하면 duplicated triplet을 방지할 수 있다.
        """

        n = len(nums)
        res = []

        # nums 오름차순 정렬
        nums.sort()

        for i in range(n - 2):  # -- 하나의 값 고정
            # 고정한 값이 이전에 나왔던 값이면 빠르게 넘어가기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 고정된 값보다 큰 값 범위에서, 양 끝에서부터 좁혀오며 확인
            j, k = i + 1, n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]

                # (1) _sum이 0보다 크면 k를 왼쪽으로 한 칸 이동
                if _sum > 0:
                    k -= 1
                # (2) _sum이 0보다 작으면 j를 오른쪽으로 한 칸 이동
                elif _sum < 0:
                    j += 1
                # (3) _sum이 0이라면 res에 추가
                else:
                    triplet = [nums[i], nums[j], nums[k]]
                    res.append(triplet)

                    # 중복 원소 건너뛰기 (j는 오른쪽으로, k는 왼쪽으로)
                    while j < k and nums[j] == triplet[1]:
                        j += 1
                    while j < k and nums[k] == triplet[2]:
                        k -= 1

        return res

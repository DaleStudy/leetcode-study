class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            # 양수인 경우 더 이상 탐색할 필요가 없음
            if nums[i] > 0:
                break
            
            # i 중복 skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))

                    # 중복 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 중복 건너뛰기
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
    
        return [list(t) for t in result]

    
"""
================================================================================
풀이 과정 - 10:51 시작
================================================================================

1. 정수 배열 nums가 주어지면
2. 모든 세 쌍 [nums[i], nums[j], nums[k]]을 반환해야한다
3. i != j, i != k, j != k 여야하고
4. nums[i] + nums[j] + nums[k] == 0 이어야한다
5. 중복된 세 쌍이 포함되지 않아야한다


[1차 시도] Brute Force 3중 반복문
────────────────────────────────────────────────────────────────────────────────
6. 제약을 무시하고 생각해보면 Brute Force 3중 반복문으로 찾을 수 있을 것 같음
7. 중복도 제거해야하니까 마지막에 set을 두고 처리

        result = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted([nums[i], nums[j], nums[k]])
                        if triplet not in result:
                            result.append(triplet)

        return result

8. Time Limit Exceeded 발생
9. O(n³) 시간 복잡도로 너무 느림


[2차 시도] Two Sum 응용 (HashSet)
────────────────────────────────────────────────────────────────────────────────
10. 3개를 동시에 찾으려니까 어려운 것 같은데
11. 2개를 먼저 구하고, 나머지 하나를 더하면 0이 되는지를 확인해볼까
12. 두 수의 합 = 나머지 하나의 값
13. -nums[i] = nums[j] + nums[k]
14. 그럼 Two Sum 문제로 풀 수 있을듯?
15. 두 개의 합이 set에 존재하는지를 체크하는 형태로 가보자

        result = set()

        for i in range(len(nums)):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    result.add(tuple(sorted([nums[i], nums[j], complement])))
                seen.add(nums[j])

        return [list(x) for x in result]

16. 아 근데 이것도 Time Limit Exceeded가 발생하네
17. O(n²) 시간 복잡도로 개선했지만 sorted() 호출과 set 연산이 추가 비용 발생
18. 다른 접근 방법이 필요할 듯


[3차 시도] Two Pointer 방식
────────────────────────────────────────────────────────────────────────────────
19. 그럼 Two Pointer 방식으로 풀어야할 것 같은데
20. Two Pointer 방식을 사용하려면 정렬이 필요함
21. Two Sum의 Two Pointer 패턴을 생각해보자
22. 근데 3개를 동시에 찾으려면 어떻게 해야할까?
23. i를 고정하고, 나머지에서 Two Sum으로 합이 -nums[i]인 두 수를 찾는다!

        정렬 전: [-1, 0, 1, 2, -1, -4]
        정렬 후: [-4, -1, -1, 0, 1, 2]
        index:    0   1   2  3  4  5

        i = 0, left = i + 1, right = len(nums) - 1
        [-4, -1, -1, 0, 1, 2]
         i   L              R

        i = 1:
        [-4, -1, -1, 0, 1, 2]
              i   L         R

25. 정렬 먼저 한 후 합의 크기에 따라 포인터를 이동

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(t) for t in result]

25. O(n²) 시간 복잡도 (정렬 O(n log n) + 반복문 O(n²))
26. 정상적으로 통과되는 것 확인 완료
27. 근데 이 방식으로 풀었는데 느리다


[4차 개선] 중복 제거 최적화
────────────────────────────────────────────────────────────────────────────────
28. Claude에게 물어보니 tuple 생성할 때 상수 배수가 큰 것 같다고 함
29. 중복을 미리 스킵해주는 방법을 알려줌
30. i가 양수인 경우 더 이상 탐색할 필요 없음 (정렬되어 있으므로)
31. i, left, right 중복 건너뛰기 추가

        nums.sort()
        result = set()

        for i in range(len(nums) - 2):
            # 양수인 경우 더 이상 탐색할 필요가 없음
            if nums[i] > 0:
                break

            # i 중복 skip
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))

                    # 중복 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(t) for t in result]

32. 중복 처리 최적화로 속도 개선
33. 최종 통과 확인 완료
"""

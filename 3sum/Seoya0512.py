from typing import List

'''
1차 시도: 실패 (시간 초과)
- nums에서 두 수 (A,B)를 고른 후, 세번째 숫자인 -(A+B)가 A,B를 제외한 nums에 존재하는지 확인
- 중복된 결과를 제거하기 위해 set과 sorted(tuple)을 활용

시간 복잡도: O(N^3)
- Outer loop와 Inner loop 각각 O(N) 이므로 O(N^2)은 기본
- nums[j:]에서 third_num을 찾는 데 O(N) 시간이 걸려서 전체 시간 복잡도는 O(N^3)

공간 복잡도: 최대 O(N^2)
- answer_set은 중복되지 않는 triplet을 저장하며, 3SUM 특성상 유니크한 triplet의 최대 개수는 O(N^2)

'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_set = set()

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                    third_num = -1 * (nums[i] + nums[j])   

                    if third_num in nums[j:]:
                        answer_set.add(tuple(sorted([nums[i], nums[j], third_num])))

        return [list(t) for t in answer_set]

'''
개선 : if third_num in nums[j:] 부분을 set을 활용
Approach
- nums에서 두 수 (A,B)를 고른 후, 세번째 숫자인 -(A+B)가 존재하는지 확인하는 기존 기조는 유지함
- (A,B) 쌍 중 ‘A(첫 번째 숫자)’가 동일한 값일 때,
  이미 동일한 first 값으로 생성할 수 있는 모든 triplet을 처리했으므로
  다시 같은 first로 시작하는 조합을 만들 필요가 없다는 점을 활용
- seen set을 활용해서 (A,B)가 고정된 이후 세번째 숫자인 -(A+B)가 존재하는지 O(1) 시간에 확인

- (예시) seen set은 i가 고정된 이후 j를 순회하면서 nums[j] 값을 저장
- nums = [a, b, c, d, e]
    - i = 0 (nums[i] = a)일 때, seen = {}
    - j = 1 (nums[j] = b)일 때, seen = {b}
    - j = 2 (nums[j] = c)일 때, seen = {b, c}
    - j = 3 (nums[j] = d)일 때, seen = {b, c, d}
    - j = 4 (nums[j] = e)일 때, seen = {b, c, d, e)

시간 복잡도: O(N^2)
- Outer loop와 Inner loop 각각 O(N) 이므로 전체 시간 복잡도는 O(N^2)

공간 복잡도: 최대 O(N^2)
- seen set은 nums[j]를 저장하며 최악의 경우 O(N)
- used_first도 distinct first 값들을 저장하며 최대 O(N)
- answer_set은 중복되지 않는 triplet을 저장하며, 3SUM 특성상 유니크한 triplet의 최대 개수는 O(N^2)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer_set = set()
        n = len(nums)

        used_first = set()  # 이미 i로 사용한 값들

        for i in range(n - 1):
            # 같은 값을 첫 번째 숫자로 한 번만 쓰기
            if nums[i] in used_first:
                continue
            used_first.add(nums[i])

            seen = set()
            for j in range(i + 1, n):
                third_num = -1 * (nums[i] + nums[j])

                if third_num in seen:
                    triplet = tuple(sorted([nums[i], nums[j], third_num]))
                    answer_set.add(triplet)
                else:
                    seen.add(nums[j])

        return [list(t) for t in answer_set]

'''
풀이
- 중복되는 triplet을 피하기 위해 배열 nums를 정렬합니다
- nums를 순회하며 이중 반복문을 수행하여 res 배열을 만듭니다
- 중복되는 triplet을 피하기 위해 appended set을 이용합니다

Big O
- N: 배열 nums의 크기

- Time complexity: O(N^2)
  - nums를 정렬하는데 걸리는 시간은 NlogN 형태로 증가합니다
  - 이중 반복문을 실행하는데 걸리는 시간은 N^2 형태로 증가합니다
  - O(NlogN + N^2)에서 증가율이 가장 큰 항은 N^2이므로 시간복잡도는 O(N^2)이라고 볼 수 있습니다

- Space complexity: O(N)
  - nums를 정렬한 배열을 복사하여 sorted_nums에 저장하였고 이에 필요한 공간은 N의 형태로 증가합니다
  - 첫번째 반복문 안의 store은 최대 N만큼 커질 수 있습니다
  - appended 집합은 nums의 모든 원소가 고유하더라도 N보다 커질 수 없습니다
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        sorted_nums = sorted(nums)

        res = []

        for i in range(n - 2):
            first = sorted_nums[i]
            
            if i > 0 and first == sorted_nums[i - 1]:
                continue
            
            store = {}
            store[-first - sorted_nums[i + 1]] = sorted_nums[i + 1]

            appended = set()

            for j in range(i + 2, n):
                second = sorted_nums[j]

                if second in store and second not in appended:
                    res.append([first, store[second], second])
                    appended.add(second)
                store[-first - second] = second
        
        return res

"""
Inputs: 정수 배열 nums

Outputs: triplet 모음 배열 (중복 요소 X)

Constraints: 3 < = nums.length <= 3 * 10^3
-10^5 <= nums[i] <= 10^5

Time Complexity:

각 수들의 위치 다르면서, 합이 0이 되는 조합들의 모음 결과
n^3 은 안됨

하지만 가능한 모든 조합 구하기를 효율화 시키면 될듯?

x 0 1 2 3 4 5
0 [_,-1,0,1,-2,-5]
1 [_,_,1,2,-1,-4]
2 [_,_,_,
3
4
5

n^2



0 [1 2]
0 [1 3]
0 [1 4]
0 [1 5]

0 1 [2 3]
0 1 [2 4]
0 1 [2 5]

0 1 2[3 4]
0 1 2[3 5]

0 1 2 3 [4 5]

우선 대괄호 안 두 수 합 사전 만들고,
keys() 순회하며,
key = a, b -> a보다 작은 수 for문 돌며 합 구하기?
-> 그럼 시간복잡도 : O(n^3 보다 살짝 작은??)

하지만 이 풀이로는 중복 후보가 나옴..


Space Complexity: O(n^2)

대괄호 내 두 수 조합 만큼의 크기가 사전 크기

# 1차 제출 코드

from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        v = defaultdict(int)
        ret = []
        memo = set()

        for i in range(1, n):
            for j in range(i + 1, n):
                v[(i, j)] = nums[i] + nums[j]

        print(v)
        for key in v.keys():
            a, b = key
            print('key: a, b', a, b)

            for i in range(a):
                if nums[i] + v[key] == 0 and \
                    not (nums[i] in memo and nums[a] in memo and nums[b] in memo):
                    print('sum zero!')
                    memo.add(nums[i])
                    memo.add(nums[a])
                    memo.add(nums[b])
                    ret.append([nums[i], nums[a], nums[b]])



        return ret

테스트 케이스만 정답..
nums =
[-1,0,1,2,-1,-4,-2,-3,3,0,4] 인 경우는 오답

[회고]
완탐, dp로 해봐도 안 풀리면 투 포인터 생각해보기!
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tuples = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else :
                    tuples.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return list(tuples)


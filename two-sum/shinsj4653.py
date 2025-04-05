"""
# Constraints

2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

같은 숫자 두번 사용 X

# Time Complexity: O(n)

O(n^2) 으로도 가능은 하지만, 문제에서 이거보다 더 적은 시간복잡도로 풀 수도 있다는 말이 존재
배열 순회하며
첫 원소는 target - n 을 한 값을 set에 넣어두기
다음 원소부터는 해당 값이 set에 있는지 체크
없다면 target - n 넣기

근데 생각해보니 원소의 "idx" 를 반환해야함
-> set대신 dict를 써서,
-> dict[value] = idx로 구성
-> dict[7] = 0
-> 배열 7 오면, 현재 idx랑 기존 idx 가져오기 가능!

# Space Complexity: O(n)

배열 원소 개수만큼 target - n 값이 들어갈 set 크기가 결정됨

"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        diffDict = dict()

        diffDict[target - nums[0]] = 0

        for i in range(1, len(nums)):
            if nums[i] in diffDict:
                ret.append(diffDict[nums[i]])
                ret.append(i)
                return ret

            else:
                diffDict[target - nums[i]] = i
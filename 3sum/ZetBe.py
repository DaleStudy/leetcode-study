'''
문제: 중복되지 않는 세 수의 조합으로 합이 0이 되는 모든 경우를 찾기
풀이: 정렬된 배열에서 첫 번째 수를 고정하고, 나머지 두 수를 투 포인터로 탐색
시간복잡도: O(n^2)
    배열을 정렬하는데 O(n log n), O(n)으로 순회하며 각 수에 대해 투 포인터로 나머지 두 수를 찾는데 O(n)이므로 전체 시간복잡도는 O(n^2)이다.
공간복잡도: O(1)
    추가적인 공간을 사용하지 않으므로 전체 공간복잡도는 O(1)이다.
사용한 자료구조: 리스트

별도의 회고: 정답에 중복된 조합이 들어가지 않도록 하기 위해,
첫 번째 수를 고정할 때 이전 수와 같은 경우를 건너뛰고, 나머지 두 수를 찾을 때도 세 수의 합이 0일 경우, 각 두 동일한 수가 연속으로 나오는 경우를 건너뛰도록 하였다.
'''

import ast
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    arr = [nums[i], nums[l], nums[r]]
                    answer.append(arr[:])
                    while l < r and nums[l] == nums[l + 1]: 
                        l+=1
                    while l < r and nums[r] == nums[r - 1]: 
                        r-=1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            
        
        

        return answer
    


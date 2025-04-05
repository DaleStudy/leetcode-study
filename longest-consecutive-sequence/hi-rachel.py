# 처음 풀이
# O(n log n) time, O(n) space

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        nums.sort()
        result = []
        cnt = 1

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cnt += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                result.append(cnt)
                cnt = 1
        result.append(cnt)
        
        return max(result)

# 공간 복잡도 O(1) 개선 풀이
# result 배열 사용시 최악의 경우 최대 n개의 숫자가 저장되므로 O(n) 공간 사용
# longest 정수 변수 사용시 상수 공간 사용

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: # pythonic code
            return 0
        
        nums.sort()
        longest = 0
        cnt = 1

        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cnt += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                longest = max(cnt, longest)
                cnt = 1
        longest = max(cnt, longest)
        
        return longest
    
# 시간 복잡도 O(n) 개선 풀이
# 현재 문제의 요구사항은 시간 복잡도 O(n)이었으므로, 위에 풀이들은 틀렸음 (You must write an algorithm that runs in O(n) time.)
# O(n) time, O(n) space -> 리트 코드 통과 x

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 in num_set:
                continue
            cnt = 1
            while num + cnt in num_set:
                cnt += 1
            longest = max(cnt, longest)

        return longest
    

# 최종 개선 풀이
# O(n) time, O(n) space
# 위 풀이에서 한쪽으로 구간을 찾지 않고, 양쪽으로 찾으며 숫자를 집합에서 제거하며
# 집합에서 원소가 하나도 남지 않을 때까지 하면 가장 긴 구간의 길이를 구할 수 있다.
# 배열의 모든 정수를 set에 저장했으므로 공간 복잡도는 O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        
        while num_set:
            num = num_set.pop()
            left, right = 1, 1
            
            while num - left in num_set:
                num_set.remove(num - left)
                left += 1
            
            while num + right in num_set:
                num_set.remove(num + right)
                right += 1
            longest = max(left + right - 1, longest)
        
        return longest
    
# TS 풀이
# O(n) time, O(n) space
# JavaScript Set에서 값을 꺼내고자 할때는 **numSet.values().next().value** 사용

# function longestConsecutive(nums: number[]): number {
#     let numSet = new Set(nums);
#     let longest = 0;

#     while (numSet.size !== 0) {
#         let num = numSet.values().next().value;
#         numSet.delete(num);
#         let [left, right] = [1, 1];

#         while (numSet.has(num - left)) {
#             numSet.delete(num - left);
#             left += 1;
#         }

#         while (numSet.has(num + right)) {
#             numSet.delete(num + right);
#             right += 1;
#         }
#         longest = Math.max(left + right - 1, longest);
#     }
#     return longest;
# };
# 30분 내로 풀지 못함. 풀이를 참고하였음.
# idea : x - 1 이 존재하지 않는 x 값에서만 loop 를 실행한다.
# time O(n) : 모든 숫자를 많아야 1,2번 방문.
# space O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        answer = 0
        for num in s:
            if num - 1 not in s:
                cur = num - 1
                length = 0
                while cur + 1 in s:
                    cur = cur + 1
                    length = length + 1
                answer = max(answer , length)

        return answer



# 정렬하면 쉬운데 O(n)이 필요하네 → set으로 조회를 O(1)로 → 근데 중복으로 세네 → 시작점에서만 세자

# TC : O(n)
# SC : O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)

        ans = 0
        
        for num in s:
            if num - 1 in s:
                continue
            
            sub_ans = 1
            next_num = num + 1
            while next_num in s:
                sub_ans = sub_ans + 1
                next_num = next_num + 1
            ans = max(ans, sub_ans)
        
        return ans

            



# 2차 풀이
class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)

        max_cnt = 0
        for n in ss:
            # 연속점의 시작점이 아닐 경우 패스
            if n-1 in ss:
                continue
            
            # 연속점의 시작점일 때만 실행되는 로직이므로
            # 숫자를 하나씩 증가시켜보면서 체크
            cnt = 1
            i = n+1
            while i in ss:
                i += 1
                cnt += 1
            
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt


# 1차 풀이
class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        ss = set(nums)
        visit = set()

        max_cnt = 0
        for n in ss:
            if n in visit:
                continue
            visit.add(n)

            cnt = 1
            
            i = n+1
            while i in ss:
                visit.add(i)
                i += 1
                cnt += 1

            i = n-1
            while i in ss:
                visit.add(i)
                cnt += 1
                i -= 1
            
            max_cnt = max(max_cnt, cnt)
        
        return max_cnt

"""
    풀이 : 
        오름차순으로 interval을 정렬 후 ans의 마지막과 interval을 비교
            - 겹치는 구간이 있다면 합치고
            - 없다면 ans에 새로 interval을 추가한다
        
        - 정렬을 쓰지 않고 풀었을 때:
            이중for문으로 비교하면서 merged라는 set로 중복검사되지 않도록 유의하면서 합친다
            겹치는 구간 또한 정렬되어 있지 않기 때문에 좀 더 복잡한 조건으로 비교해야함

    interval 수 N

    TC : O(N logN)
        정렬하는데 들어가는 시간 N logN + for문 N
    
    SC : O(N)
        sorted(intervals)는 N에 비례, 결과 배열은 최악의 경우 N과 동일일
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals):
            if not ans:
                ans.append(interval)
            if interval[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], interval[1])
            else :
                ans.append(interval)
        return ans

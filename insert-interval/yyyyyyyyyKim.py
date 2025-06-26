class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # 시간복잡도 O(n log n), 공간복잡도 O(n)

        # newInterval 추가하고 정렬
        intervals.append(newInterval)
        intervals.sort()

        answer = [intervals[0]]
        
        for i in range(1, len(intervals)):
            prev = answer[-1]
            curr = intervals[i]

            # 병합하기
            # answer의 끝 값보다 현재의 시작값이 더 작으면 겹치는 것 -> 현재의 끝값과 answer의 끝값 중 더 큰 값으로 병합
            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            
            # 겹치지 않으면 현재값을 answer에 추가
            else:
                answer.append(curr)

        return answer

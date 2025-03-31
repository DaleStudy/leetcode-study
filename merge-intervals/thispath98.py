class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Intuition:
            정렬된 intervals을 순회하면서 이전의 인터벌과 현재 인터벌이
            겹친다면, 이를 갱신해준다.
            겹치지 않는다면, 새로운 인터벌을 추가한다.

        Time Complexity:
            O(N log N):
                최초에 정렬을 하므로, O(N log N)이다.
                이후 한번 스캔을 하므로 O(N)이다.
                따라서 시간 복잡도는 O(N log N)이다.

        Space Complexity:
            O(N):
                answer에 N개의 값을 저장하므로 O(N)이다.
        """
        sorted_intervals = sorted(intervals)

        answer = [sorted_intervals[0]]
        for start, end in sorted_intervals[1:]:
            prev_start, prev_end = answer[-1]
            if prev_end >= start:
                answer[-1][1] = max(prev_end, end)
            else:
                answer.append([start, end])
        return answer

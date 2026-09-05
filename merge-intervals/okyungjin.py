'''
https://leetcode.com/problems/merge-intervals/description/

N: len(intervals)
Time: O(N logN), 정렬
Space: O(N), answer 배열
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        answer = [intervals[0]]

        '''
        [1,4], [5,8] # case A
        [1,4], [4,7] # case B
        [1,4], [2,8] # case C
        '''

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            _, last_end = answer[-1]

            if curr_start > last_end: # case A
                answer.append(intervals[i])
            elif curr_end > last_end: # case C
                answer[-1][1] = curr_end

        return answer

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # # first structure it as graph (dictionary)
        # intervals = [[1,2],[2,3],[3,4],[1,3]]
        # dict = {}
        # for i in intervals:
        #     dict[i[0]] = []
        # for a,b in intervals:
        #     dict[a].append(b)

        # #Overlapping edge cases
        # # 1. [1,4], [2,3] -> not sure how to figure out 
        # # 2. [1,3], [1,2] , [3,4] -> check if the value has connection 
        # # 3. [1,2], [1,2], [1,2] ( same values) use hashset 

        # count = 0 
        # visited = set()
        # for key, value in dict.items():
        #     if value not in visited:
        #         visited.append(value)
        #     else:
        #         count += 1
        # return count

        # count = 0 
        # visited = set()
        # for a, b in intervals:
        #     if b not in visited:
        #         visited.add(b)
        #     else:
        #         count += 1
        # return count 


        # greedy Approach 
        intervals.sort()

        res = 0 
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)
        return res

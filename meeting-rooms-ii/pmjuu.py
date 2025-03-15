'''
시간 복잡도: O(n log n)
공간 복잡도: O(n)
'''
from typing import List
from heapq import heappush, heappop

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:x.start)
        ends = []

        for interval in intervals:
            if ends and ends[0] <= interval.start:
                heappop(ends)

            heappush(ends, interval.end)
        
        return len(ends)
    

def run_tests():
    solution = Solution()
    
    test_cases = [
        # Test Case 1: 문제의 Example 1
        {
            "input": [Interval(0, 30), Interval(5, 10), Interval(15, 20)],
            "expected": 2,
            "description": "Example 1: [(0,30), (5,10), (15,20)] - 2 rooms needed"
        },
        # Test Case 2: 문제의 Example 2
        {
            "input": [Interval(2, 7)],
            "expected": 1,
            "description": "Example 2: [(2,7)] - 1 room needed"
        },
        # Test Case 3: 겹치지 않는 회의들
        {
            "input": [Interval(0, 8), Interval(8, 10), Interval(10, 12)],
            "expected": 1,
            "description": "Non-overlapping meetings: [(0,8), (8,10), (10,12)]"
        },
        # Test Case 4: 모든 회의가 겹치는 경우
        {
            "input": [Interval(1, 5), Interval(2, 6), Interval(3, 7)],
            "expected": 3,
            "description": "All overlapping: [(1,5), (2,6), (3,7)]"
        },
        # Test Case 5: 빈 입력
        {
            "input": [],
            "expected": 0,
            "description": "Empty input: []"
        },
        # Test Case 6: 복잡한 경우
        {
            "input": [Interval(1, 10), Interval(2, 7), Interval(3, 19), Interval(8, 12)],
            "expected": 3,
            "description": "Complex case: [(1,10), (2,7), (3,19), (8,12)]"
        },
        {
            "input": [Interval(1, 4), Interval(2, 5), Interval(3, 6)],
            "expected": 3,
            "description": "Multiple overlaps: [(1,4), (2,5), (3,6)]"
        },
        {
            "input": [Interval(1, 10), Interval(2, 3), Interval(4, 5), Interval(6, 7)],
            "expected": 2,
            "description": "Short and long meetings: [(1,10), (2,3), (4,5), (6,7)]"
        },
        {
            "input": [Interval(1, 5), Interval(5, 10), Interval(10, 15), Interval(2, 7)],
            "expected": 2,
            "description": "Mixed overlaps: [(1,5), (5,10), (10,15), (2,7)]"
        }
    ]

    # 테스트 실행
    for i, test in enumerate(test_cases, 1):
        intervals = test["input"]
        expected = test["expected"]
        result = solution.min_meeting_rooms(intervals)
        
        print(f"Test Case {i}: {test['description']}")
        print(f"Input: {[(interval.start, interval.end) for interval in intervals]}")
        print(f"Expected Output: {expected}")
        print(f"Your Output: {result}")
        print(f"Result: {'✅ PASS' if result == expected else '❌ FAIL'}")
        print("-" * 50)

if __name__ == "__main__":
    run_tests()

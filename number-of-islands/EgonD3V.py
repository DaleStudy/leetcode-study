from collections import deque
from typing import Generic, List, Optional, TypeVar
from unittest import TestCase, main


T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.prev = None
        self.post = None


class Deque(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def appendright(self, value: T):
        node = Node(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            if self.tail:
                self.tail.post = node
            self.tail = node
        self.size += 1

    def appendleft(self, value: T):
        node = Node(value)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.post = self.head
            if self.head:
                self.head.prev = node
            self.head = node
        self.size += 1

    def popright(self) -> T:
        if self.is_empty():
            raise IndexError("Deque is empty!")

        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.post = None
        else:
            self.head = None
        self.size -= 1
        return value

    def popleft(self) -> T:
        if self.is_empty():
            raise IndexError("Deque is empty!")

        value = self.head.value
        self.head = self.head.post
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.size -= 1
        return value


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        return self.solve_bfs_custom(grid)

    """
    Runtime: 243 ms (Beats 60.00%)
    Time Complexity: O(MAX_R * MAX_C)
        - 2차원 배열 grid를 조회하며 deq에 enqueue하는데 O(MAX_R * MAX_C)
            - deq의 원소 하나 당 DIRS 크기만큼 탐색에 O(4), 원소에 해당하는 grid의 값이 "0"인 경우 탐색하지 않으므로 upper bound
            - deque의 appendleft, popleft에 O(1)
        > O(MAX_R * MAX_C) * O(4) ~= O(MAX_R * MAX_C)

    Memory: 18.82 (Beats 83.56%)
    Space Complexity: O(MAX_R * MAX_C)
        - visited 역할을 grid의 원소의 값을 변경하여 사용하였으므로 무시
        - deque의 최대 크기는 MAX_R * MAX_C 이므로 O(MAX_R * MAX_C), upper bound
        > O(MAX_R * MAX_C)
    """
    def solve_bfs(self, grid: List[List[str]]) -> int:

        def is_island(r: int, c: int) -> bool:
            nonlocal grid

            if grid[r][c] != "1":
                return False

            deq = deque([(r, c)])
            deq.appendleft((r, c))
            while deq:
                curr_r, curr_c = deq.popleft()
                grid[r][c] = "0"
                for dir_r, dir_c in DIRS:
                    post_r, post_c = curr_r + dir_r, curr_c + dir_c
                    if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and grid[post_r][post_c] == "1":
                        grid[post_r][post_c] = "0"
                        deq.appendleft((post_r, post_c))

            return True

        MAX_R, MAX_C = len(grid), len(grid[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        count = 0
        for r in range(MAX_R):
            for c in range(MAX_C):
                count += 1 if is_island(r, c) else 0
        return count

    """
    Runtime: 283 ms (Beats 23.05%)
    Time Complexity: O(MAX_R * MAX_C)
        > solve_bfs와 동일
    Memory: 19.98 (Beats 44.38%)
    Space Complexity: O(MAX_R * MAX_C)
        > solve_bfs와 동일
    """
    def solve_bfs_custom(self, grid: List[List[str]]) -> int:

        def is_island(r: int, c: int) -> bool:
            nonlocal grid

            if grid[r][c] != "1":
                return False

            deq = Deque()
            deq.appendleft((r, c))
            while not deq.is_empty():
                curr_r, curr_c = deq.popleft()
                grid[r][c] = "0"
                for dir_r, dir_c in DIRS:
                    post_r, post_c = curr_r + dir_r, curr_c + dir_c
                    if 0 <= post_r < MAX_R and 0 <= post_c < MAX_C and grid[post_r][post_c] == "1":
                        grid[post_r][post_c] = "0"
                        deq.appendleft((post_r, post_c))

            return True

        MAX_R, MAX_C = len(grid), len(grid[0])
        DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))
        count = 0
        for r in range(MAX_R):
            for c in range(MAX_C):
                count += 1 if is_island(r, c) else 0
        return count


class _LeetCodeTestCases(TestCase):
    def test_1(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        output = 3
        self.assertEqual(Solution.numIslands(Solution(), grid), output)


if __name__ == '__main__':
    main()

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pass


if __name__ == "__main__":

    test_cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [], True),
        (4, [[1, 0], [2, 1], [3, 2]], True),
        (5, [[1, 0], [2, 0], [3, 1], [3, 2], [4, 3]], True),
        (1, [[0, 0]], False),
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),
    ]

    solution = Solution()

    for idx, (numCourses, prerequisites, expected) in enumerate(test_cases, start=1):

        result = solution.canFinish(numCourses, prerequisites)

        assert (
            result == expected
        ), f"Test Case {idx} Failed: Expected {expected}, Got {result}"

    print("All test cases passed.")

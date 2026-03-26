from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        character_map = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        s_stack = deque()

        for c in s:
            if c in character_map.keys():
                s_stack.append(c)

            else:
                if len(s_stack) > 0:
                    previous = s_stack.pop()
                    if character_map[previous] != c:
                        return False
                else:
                    return False

        if len(s_stack) > 0:
            return False
        else:
            return True


if __name__ == "__main__":
    test_cases = [
        ("{{{[[[(([{{}}]))]]]}}}", True),
        ("{{{]}}", False),
        ("{", False),
        ("}}]", False),
        ("{}[]()", True),
        ("{[]}[()]", True),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        s, answer = case_
        result = solution.isValid(s)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"

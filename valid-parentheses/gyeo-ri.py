class Solution:
    def isValid(self, s: str) -> bool:
        character_map = {"(": ")", "{": "}", "[": "]"}
        s_list = []

        for c in s:
            if c in character_map:
                s_list.append(character_map[c])

            else:
                if len(s_list) > 0:
                    if s_list.pop() == c:
                        continue
                return False

        return len(s_list) == 0


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

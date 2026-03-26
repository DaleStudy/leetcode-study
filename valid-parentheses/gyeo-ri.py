"""
[결과 요약]
# 재시도횟수: 3회
    1. 조건에는 맞지만 메모리를 많이 사용 / 빈번한 False 리턴을 사용한 방법:: O(n)/O(n)
    2. 1의 로직의 가독성과 메모리 사용량 개선하기: O(n)/O(n)
    3. 실제로는 if/else문으로 풀어도 최적의 성능이 나오면서 가독성 측면에서도 유리: : O(n)/O(n)
"""


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


"""
# 실제로는 복잡한 로직 없이 if/else로 직접 비교하는 쪽이 성능과 코드 가독성 면에서 모두 유리
class Solution:
    def isValid(self, s: str) -> bool:
        s_list = []

        for c in s:
            if c == '(':
                s_list.append(')')
            elif c == '{':
                s_list.append('}')
            elif c == '[':
                s_list.append(']')
            else:
                if not s_list or s_list.pop() != c:
                    return False
"""


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

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Intuition:
            stack 자료구조를 사용해서 닫히는 괄호가 올 경우
            stack의 마지막과 일치하는지 확인한다.

        Time Complexity:
            O(N):
                문자열을 한번 스캔하면서 조건문을 확인하므로
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                최악의 경우 문자열 개수만큼 stack에 저장한다.
        """
        stack = []
        for ch in s:
            if ch in ["(", "{", "["]:
                stack.append(ch)
            elif ch in [")", "}", "]"]:
                if stack and (
                    (ch == ")" and stack[-1] == "(")
                    or (ch == "}" and stack[-1] == "{")
                    or (ch == "]" and stack[-1] == "[")
                ):
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        else:
            return True

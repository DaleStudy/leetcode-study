class Solution:
    def isValid(self, s: str) -> bool:
        """s에 있는 bracket들의 쌍이 맞는지 확인하는 함수
        시간 복잡도: O(n), 공간 복잡도: O(n)

        Args:
            s (str): bracket {}, [], ()로 이루어진 문자열

        Returns:
            bool: bracket들의 쌍이 맞는지 여부
        """
        stack = []
        pair = {"{": "}", "[": "]", "(": ")"}
        for ch in s:
            if ch in pair:
                stack.append(ch)
            elif len(stack) == 0:
                return False
            else:
                last = stack.pop()
                if pair[last] != ch:
                    return False
        return True if len(stack) == 0 else False

class Solution:
    def isValid(self, s: str) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)
        opens = ['(', '[', '{']
        closes = [')', ']', '}']
        required = []
        pair = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        answer = True
        for elem in s:
            if elem in opens:
                required.append(pair[elem])
            else:
                if elem in required and required[-1] == elem:
                    required.pop()
                else:
                    answer = False
                    break
        return True if (answer and len(required) == 0) else False

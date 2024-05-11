### Intuition
- opening(`([{`) 스택을 쌓는다.
- 비교한다.

### Approach
1. 먼저 입력받은 글자의 길이가 짝수가 아니면 무조건 **False**.
2. for 문
    - opening(`([{`) 이면 stack 에 넣는다.
    - stack 이 비어있거나, 짝이 맞지 않으면(`is_parentheses()==False`) **False**.
3. 다 완료되고 나서, 스택이 비어있다면 **True**.


### Complexity
- Time complexity: O(n)
- Space complexity: O(n)


### Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0:
            return False
        for word in s:
            if word in '([{':
                stack.append(word)
            elif not stack or is_parentheses(stack.pop(), word) is False:
                return False
        return not stack


def is_parentheses(pointer, word) -> bool:
    if pointer == '(' and word == ')':
        return True
    elif pointer == '[' and word == ']':
        return True
    elif pointer == '{' and word == '}':
        return True
    else: return False
```

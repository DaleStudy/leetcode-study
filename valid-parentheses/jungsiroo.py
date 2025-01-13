class Solution:
    def isValid(self, s: str) -> bool:
        """
        스택을 이용한 간단한 풀이

        s에 포함될 괄호들은 이미 정해져있는 상태이기에 딕셔너리 이용
        이를 이용해 stack의 마지막 원소가 현재 괄호와 매치되는지를 정수를 통해 알 수 있음

        마지막은 stack이 전부 비었을 때 True를 리턴

        Time Complexity : O(n)
        Space Complexity : O(n) (stack 변수)
        """


        chars = {'(':1, '{':2, '[':3, ')':-1, '}':-2, ']':-3}
        stack = []

        for char in s:
            if chars[char] > 0:
                stack.append(char)
            else:
                if not stack : return False
                
                if chars[stack[-1]] == -chars[char]:
                    stack.pop()
                else:
                    return False
                    
        return not stack
        
        

class Solution:
    def isValid(self, s: str) -> bool:
        '''
        문제: string s 에 대해서 valid parentheses 이면 true 아니면 false
        conditions
        - open brackets must be closed by the same type 
        - // must be closed in the correct order
        - s 최소 길이 = 1, 최대 10^4
        solution
        - open brackets -> st array 에 저장, close brackets -> st.pop -> check valid
        - 마지막에 st array length 가 1 이상이면 return False

        - time complexity: O(n)
        - space complexity: O(n)
        '''
        
        st = []
    
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
            else:
                # check if st is empty
                if len(st) <= 0:
                    return False
                cur = st.pop()
                if s[i] == ')' and cur != '(':
                    return False
                if s[i] == '}' and cur != '{':
                    return False
                if s[i] == ']' and cur != '[':
                    return False
        if len(st) > 0:
            return False
        return True

        

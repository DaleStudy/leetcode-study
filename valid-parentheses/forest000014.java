/*
Time Complexity: O(n)
Space Complexity: O(n)

유효한 문자열이라면, 인접한 열고 닫는 괄호 쌍을 하나씩 캔슬시켰을 때, 빈 문자열만 남게 된다.
매치되는 쌍이 서로 떨어져있을 수 있기 때문에, 그 안의 유효한 쌍들을 미리 모두 캔슬시킨 뒤에 판단해야 매칭 여부를 쉽게 판단할 수 있는데, 이 과정을 스택을 이용해 구현할 수 있다.
*/
class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();

        if (s.length() % 2 == 1) {
            return false;
        }

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (st.empty())
                    return false;
                if (ch == ')') {
                    if (st.peek() != '(')
                        return false;
                } else if (ch == '}') {
                    if (st.peek() != '{')
                        return false;
                } else {
                    if (st.peek() != '[')
                        return false;
                }
                st.pop();
            }
        }
        return st.empty();
    }
}

/**
 * 풀이
 * - stack 자료구조를 이용합니다
 * 
 * Big O
 * - N: 주어진 문자열 s의 길이
 * 
 * - Time complexity: O(N)
 *   - 문자열 s 전체를 순회할 경우 실행시간은 N에 선형적으로 비례하여 증가합니다
 * - Space complexity: O(N)
 *   - "((((((...((((((" 와 같은 입력을 받으면 stack의 크기가 최대 N까지 증가합니다
 */

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (char ch : s) {
            if (ch == '(' || ch == '{' || ch == '[') {
                st.push(ch);
            } else {
                if (st.empty()) return false;
                else if (st.top() == '(' && ch == ')') st.pop();
                else if (st.top() == '{' && ch == '}') st.pop();
                else if (st.top() == '[' && ch == ']') st.pop();
                else return false;
            }
        }
        return st.empty();
    }
};

class Solution {
public:
    bool isValid(string s) {
        stack<char> st; // 여는 괄호를 저장할 스택

        for (char ch : s)
        {
            if (isOpening(ch)) // 여는 괄호라면 스택에 push
            {
                st.push(ch);
                continue;
            }

            if (st.empty()) // 스택이 비었는데 닫는 괄호면 invalid
            {
                return false;
            }

            char t = st.top();
            st.pop();

            // 괄호 쌍이 맞으면 계속 진행
            if ((ch == ')' && t == '(')
            || (ch == ']' && t == '[')
            || (ch == '}' && t == '{'))
            {
                continue;
            }

            // 괄호 쌍이 맞지 않으면 invalid
            return false;
        }

        return st.empty();
    }

private:
    bool isOpening(char c)
    {
        switch(c)
        {
            case '(':
            case '[':
            case '{':
                return true;
        }

        return false;
    }
};

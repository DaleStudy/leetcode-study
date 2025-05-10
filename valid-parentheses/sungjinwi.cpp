/*
    
*/

class Solution {
    public:
        bool isValid(string s) {
            stack<char> st;

            for (auto& c : s)
            {
                if (c == ')')
                {
                    if (st.empty() || st.top() != '(')
                        return false;
                    st.pop();
                }
                if (c == '}')
                {
                    if (st.empty() || st.top() != '{')
                        return false;
                    st.pop();
                }
                if (c == ']')
                {
                    if (st.empty() || st.top() != '[')
                        return false;
                    st.pop();
                }
                else
                    st.push();
            }

            if (!st.empty())
                return false;
            else
                return true;
        }
    };

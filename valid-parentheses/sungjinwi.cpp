/*
    풀이 : 
        stack을 이용해서 괄호를 넣고 뺸다.
        닫는 괄호 ),],}를 만났을 때 가장 위의 괄호가 대응하는 괄호면 제거하고 비어있거나 맞지 않는 괄호면 return false
        string을 모두 순회했을 떄 stack이 비어있지 않으면 return false

    s의 길이 N

    TC : O(N)
        s에 대해 반복 1회

    SC : O(N)
        최악의 경우 stack 크기는 s의 길이에 비례
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

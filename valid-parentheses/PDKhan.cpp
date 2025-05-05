class Solution {
    public:
        bool isValid(string s) {
            stack<char> st;
    
            for(char ch : s){
                if(ch == ')'){
                    if(st.empty() || st.top() != '(')
                        return false;
                    st.pop();
                }else if(ch == '}'){
                    if(st.empty() || st.top() != '{')
                        return false;
                    st.pop();
                }else if(ch == ']'){
                    if(st.empty() || st.top() != '[')
                        return false;
                    st.pop();
                }else
                    st.push(ch);
            }
    
            return st.empty();
        }
    };

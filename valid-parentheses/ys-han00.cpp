class Solution {
public:
    bool isValid(string s) {
        stack<char> sta;
        
        for(char c : s) {
            if(c == '(' || c == '[' || c == '{') {
                sta.push(c);
                continue;
            }

            if(sta.empty())
                sta.push(c);
            else if(c == ')' && sta.top() == '(')
                sta.pop();
            else if(c == ']' && sta.top() == '[')
                sta.pop();
            else if(c == '}' && sta.top() == '{')
                sta.pop();
            else
                sta.push(c);
        }

        return (sta.empty() ? true : false);
    }
};


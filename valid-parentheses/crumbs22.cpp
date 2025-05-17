#include <iostream>
#include <stack>
#include <string>

using namespace std;

class Solution {
	public:
		bool isValid(string s) {
			stack<char> st;

			for (char c : s) {
                // if (!st.empty())
                //     cout << st.top();
				if (c == '}') {
					if (st.empty() || st.top() != '{') {
						return (false);
					}
					st.pop();
                    continue ;
				}
				else if (c == ')') {
					if (st.empty() || st.top() != '(') {
						return (false);
					}
					st.pop();
                    continue ;
				}
				else if (c == ']') {
					if (st.empty() || st.top() != '[') {
						return (false);
					}
					st.pop();
                    continue ;
				}
				st.push(c);
			}
			return (st.empty());
		}
	};

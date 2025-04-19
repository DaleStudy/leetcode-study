/*
    풀이 :
        i 번째 연산을 시작 전 cur는 i + 1에서 시작하는 경우의 수, nxt에는 i + 2에서 시작하는 경우의 수 저장돼있다
        i 번째 연산이 끝난 후 cur는 i에서 시작하는 경우, nxt에는 i + 1에서 시작하는 경우의 수 저장되도록 한다
        s의 길이가 1일 때 무조건 1개의 경우의 수를 가지므로 cur 1로 초기화
        
        세가지 경우의 수
        1. s[i]가 '0' 일때 0으로 시작하는 문자열은 해석가능한 수가 없으므로 cur를 0으로 한다
        2. s[i]로 시작하는 두 자리 수가 숫자로 변환하면 27보다 작으면, 1자리로 변환하는 경우의 수(cur) + 2자리로 변환하는 경우의 수(nxt)로 cur 변경
        3. 그 외에는 1자리로 변환하는 경우의 수 밖에 없으므로 cur 그대로

        문자열 끝에서 조건에 맞춰 업데이트 하면서 문자열 처음까지 순회하고 cur 리턴한다

    문자열 길이 N

    TC : O(N)
        문자열 한번 순회

    SC : O(1)
*/

#include <string>
using namespace std;

class Solution {
    public:
        int numDecodings(string s) {
            int cur = 1;
            int nxt = 0;
            int tmp;
    
            for (int i = s.size() - 1; i >= 0; i--)
            {
                tmp = nxt;
                if (s[i] == '0')
                {
                    nxt = cur;
                    cur = 0;
                }
                else if(i < s.size() - 1 && stoi(s.substr(i, 2)) < 27)
                {
                    nxt = cur;
                    cur = cur + tmp;
                }
                else
                {
                    nxt = cur;
                }
            }
            return cur;
        }
    };

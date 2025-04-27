/*
    풀이 :
        쉬프트 연산으로 n을 감소 시키면서 n 과 1의 & 연산이 true인 갯수를 세서 리턴
    
    TC : O(1)
        n이 커도 최대 32번의 반복문

    SC : O(1)
*/

class Solution {
    public:
        int hammingWeight(int n) {
            int cnt = 0;
            while (n > 0)
            {
                if (n & 1)
                    cnt++;
                n = n >> 1;
            }
            return cnt;
        }
    };

/*
    풀이 :
        n이 1과 2일 떄는 따로 처리, 그 외에 n번째는 prv(n - 2번째) + cur(n -1번째)로 값을 업데이트 하며 n까지 더해나감

    TC : O(N)
        n의 크기에 반복문이 비례한다
    
    SC : O(1)
        n의 크기와 상관없이 3개의 변수 사용
*/

class Solution {
public:
    int climbStairs(int n) {
        if (n == 1)
            return 1;
        if (n == 2)
            return 2;

        int prv = 1;
        int cur = 2;
        int tmp;
        for (int i = 3; i <= n; i++)
        {
            tmp = cur;
            cur = cur + prv;
            prv = tmp;
        }
        return cur;
    }
};

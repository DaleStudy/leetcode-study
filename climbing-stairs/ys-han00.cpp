class Solution {
public:
    int climbStairs(int n) {
        vector<int> fibo(46, 0);
        
        fibo[1] = 1;
        fibo[2] = 2;
        
        if(n <= 2)
            return fibo[n];

        for(int i = 3; i <= n; i++)
            fibo[i] = fibo[i - 1] + fibo[i - 2];
        
        return fibo[n];
    }
};


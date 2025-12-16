class Solution {
public:
    int climbStairs(int n) {
        std::map<int, int> stepMap;
        stepMap[1] = 1;
        stepMap[2] = 2;

        if (n == 1) {
            return stepMap[n];
        }
        
        for (int i = 3; i <= n; i++) {
            stepMap[i] = stepMap[i - 1] + stepMap[i - 2];
        }

        return stepMap[n];
    }
};

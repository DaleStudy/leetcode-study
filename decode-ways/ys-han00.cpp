// class Solution {
// public:
//     int numDecodings(string s) {
//         int n = s.size(), idx, ways, two;

//         queue<int> que;
//         vector<int> memo(n, 0);

//         if(s[0] != '0') {
//             que.push(0);
//             memo[0] = 1;
//         }

//         if(n >= 2) {
//             two = (s[0] - '0') * 10 + (s[1] - '0');
//             if(10 <= two && two <= 26) {
//                 que.push(1);
//                 memo[1] = 1;
//             }
//         }

//         while(!que.empty()) {
//             idx = que.front();
//             que.pop();

//             ways = memo[idx];

//             if(idx + 1 < n && s[idx + 1] != '0') {
//                 if(memo[idx + 1] == 0) 
//                     que.push(idx + 1);
//                 memo[idx + 1] += ways;
//             }

//             if(idx + 2 < n) {
//                 two = (s[idx + 1] - '0') * 10 + (s[idx + 2] - '0');
//                 if(10 <= two && two <= 26) {
//                     if(memo[idx + 2] == 0)
//                         que.push(idx + 2);
//                     memo[idx + 2] += ways;
//                 }
//             }
//         }

//         return memo[n - 1];
//     }
// };

// class Solution {
// public:
//     int numDecodings(string s) {
//         vector<int> dp(s.size() + 1, 1);

//         for(int i = s.size() - 1; i >=0; i--) {
//             if(s[i] == '0') {
//                 dp[i] = 0;
//                 continue;
//             }
            
//             dp[i] = dp[i + 1];
//             if(i + 1 < s.size() && (s[i] - '0') * 10 + (s[i + 1] - '0') < 27)
//                 dp[i] += dp[i + 2];
//         }

//         return dp[0];
//     }
// };

class Solution {
public:
    int numDecodings(string s) {
        int cur = 1, nxt = 0, tmp;

        for(int i = s.size() - 1; i >=0; i--) {
            if(s[i] == '0') {
                nxt = cur;
                cur = 0;
                continue;
            }
            tmp = nxt;
            nxt = cur;
            if(i + 1 < s.size() && (s[i] - '0') * 10 + (s[i + 1] - '0') < 27)
                cur += tmp;   
        }

        return cur;
    }
};


/**
 * For the length of the given string N,
 * 
 * Time complexity: O(N)
 * 
 * Space complexity: O(N)
 */

class Solution {
public:
    int numDecodings(string s) {
        if (s[0] == '0') return 0;

        int memo[s.size() + 1];

        fill(memo, memo + s.size() + 1, 0);
        memo[0] = 1;
        memo[1] = 1;

        for (int i = 2; i <= s.size(); i++) {
            int s_i = i - 1;
            if (s[s_i] != '0') memo[i] = memo[i - 1];
            int two_digits = stoi(s.substr(s_i - 1, 2));
            if (10 <= two_digits && two_digits <= 26) memo[i] += memo[i - 2];
        } 

        return memo[s.size()];
    }
};

/**
 * Space complexity O(1) solution
 */

// class Solution {
// public:
//     int numDecodings(string s) {
//         if (s[0] == '0') return 0;

//         int one_digit_memo = 1, two_digit_memo = 1;

//         for (int i = 1; i < s.size(); i++) {
//             int tmp = 0;
//             if (s[i] != '0') tmp = one_digit_memo;
//             int two_digits = stoi(s.substr(i - 1, 2));
//             if (10 <= two_digits && two_digits <= 26) tmp += two_digit_memo;
//             two_digit_memo = one_digit_memo;
//             one_digit_memo = tmp;
//         } 

//         return one_digit_memo;
//     }
// };

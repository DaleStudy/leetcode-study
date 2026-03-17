/*
    191. Number of 1 Bits

    Given a positive integer n, write a function 
    that returns the number of set bits in its binary representation 
    (also known as the Hamming weight).

    Example 1:
        Input: n = 11
        Output: 3

    Explanation:
        The input binary string 1011 has a total of three set bits.     
    
    Constraints:
        1 <= n <= 2^31 - 1
*/

// 비트 연산을 이용하여 풀기
#include <iostream>
using namespace std;

class Solution {
public:
    int hammingweight(int n) {
        unsigned int answer = 0;
        while(n>0) {
            if (n & 1)
                answer++;
            n = n >> 1;
        }
        return answer;
    }
};

int main() {
    int n;
    cin >> n;
    Solution s;

    cout << s.hammingweight(n);
}

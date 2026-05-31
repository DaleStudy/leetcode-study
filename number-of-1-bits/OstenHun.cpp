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

// 시간 복잡도 : O(logn) -> n >> 1 연산을 하기 때문에 절반씩 줄어듬
// 문제의 조건은 32bit 내의 범위이기 때문에 32번의 반복으로 항상 끝나기에 O(1)이라고 할 수 있다.
// 공간 복잡도 : O(1)
class Solution {
public:
    int hammingweight(int n) {
        unsigned int answer = 0;
        while(n>0) {
            if (n & 1)
                answer++;
            n = n >> 1;
        }

        // 처음 풀었던 풀이.
        // unsigned int answer = 0;
        // for (int i = 0; i < 32; i++) {
        //     if ((n >> i) & 1) answer++;
        // }
        
        // 생각 못 한 풀이
        // -> n & (n-1) 을 하면 가장 오른쪽 1비트를 지운다.
        // while (n > 0) {
        //     n &= (n - 1);
        //     answer++;
        // }

        return answer;
    }
};

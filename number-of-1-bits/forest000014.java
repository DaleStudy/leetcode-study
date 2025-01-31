/*
solution 1. bit operation
# Time Complexity: O(1)
  - n의 사이즈는 32 bit로 일정
  - 2 * 32 회 연산 필요
# Space Complexity: O(1)

bit를 하나씩 센다.


solution 2. bit operation (advanced)
# Time Complexity: O(1)
  - 2 * b 회 연산 필요 (b는 1인 bit의 개수) 
# Space Complexity: O(1)

n &= (n - 1) 연산을 통해, 마지막 bit를 한번에 하나씩 제거하면서 bit를 센다.
1인 bit의 개수만큼 연산을 하므로, 평균적으로 solution 1보다는 연산 횟수가 적다.


solution 3. 8-bit chunk lookup table
# Time Complexity: O(n)
  - n / 8 회 연산 필요
# Space Complexity: O(1)
  - 2^8 사이즈의 int 배열 사용

이진수 00000000 ~ 11111111 에 대해서, 각 수에 bit 1이 몇 개 등장하는지 미리 lookup table에 저장해둔다.
그리고 n을 8 bit 단위로 잘라서, loopup table에서 조회하여 누적해준다.
연산 횟수가 n / 8로 줄어든다는 장점이 있으나, lookup table을 미리 계산하거나 런타임에 계산해야 하고, lookup table 사이즈만큼의 메모리를 더 사용해야 한다는 트레이드 오프가 있다.


solution 4. population count 알고리즘
# Time Complexity: O(1)
  - 5 회 연산 필요
# Space Complexity: O(1)

각 단계를 진행할 때마다, 2, 4, 8, 16, 32 bit chunk 안의 1 bit의 개수를 센다.


solution 5. 자바 내장 함수 Integer.bitCount() 사용
# Time Complexity: O(1)
# Space Complexity: O(1)

*/
class Solution {
    // solution 1
    // public int hammingWeight(int n) {
    //     int ans = 0;
    //     while (n > 0) {
    //         ans += (n & 1);
    //         n >>= 1;
    //     }
    //     return ans;
    // }

    // solution 2
    // public int hammingWeight(int n) {
    //     int ans = 0;
    //     while (n > 0) {
    //         n &= (n - 1); // 최하위 1비트를 제거
    //         ans++;
    //     }
    //     return ans;
    // }

    // solution 3.
    // lookup table (8-bit 단위로)
    // 이 아이디어는 시간이 부족해서 구현하지 못했습니다.


    // solution 4.
    // population count 알고리즘
    // https://blog.naver.com/jinhan814/222540111549
    // http://shumin.co.kr/algorithm-hamming-weight-bit-count/
    public int hammingWeight(int n) {
        n = (n >>  1 & 0x55555555) + (n & 0x55555555);
        n = (n >>  2 & 0x33333333) + (n & 0x33333333);
        n = (n >>  4 & 0x0F0F0F0F) + (n & 0x0F0F0F0F);
        n = (n >>  8 & 0x00FF00FF) + (n & 0x00FF00FF);
        n = (n >> 16 & 0x0000FFFF) + (n & 0x0000FFFF);
        return n;
    }

    // solution 5.
    // 자바 내장 함수 사용 O(logn)
    // public int hammingWeight(int n) {
    //     return Integer.bitCount(n);
    // }
}

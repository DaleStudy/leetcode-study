/** 주어진 숫자의 Hamming weight 구하기 */
class Solution {

    // 시간복잡도: O(1), 공간복잡도: O(1), 비트 연산자 사용
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count += (n & 1);
            n >>>= 1;
        }
        return count;
    }

    // 시간복잡도: O(1), 공간복잡도: O(1)
    // public int hammingWeight(int n) {

    //     int count = 0;
    //     while (n != 0) {
    //         if (n % 2 == 1) {
    //             count++;
    //         }
    //         n /= 2;
    //     }
    //     return count;
    // }

    // 시간복잡도: O(1), 공간복잡도: O(n)
    // public int hammingWeight(int n) {
    //     return Integer.toBinaryString(n).replaceAll("0", "").length();
    // }
}


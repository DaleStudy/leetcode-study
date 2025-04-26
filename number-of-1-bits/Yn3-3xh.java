/**
 [문제풀이]
 - 주어진 양의 정수를 2진수로 변환하여, 1의 개수 구하기

 - 풀이 1
 time: O(log N), space: O(1)
     class Solution {
         public int hammingWeight(int n) {
             int count = 0;
             while (n > 0) {
                 if (n % 2 != 0) {
                    count++;
                 }
                 n /= 2;
             }
             return count;
         }
     }
 - 풀이 2
 time: O(log N), space: O(1)

 [회고]
 `n >> 1`비트 연산자는 `n / 2` 와 같다.
 `n >> 1`로 풀면 비교도 비트로!

 이진 표현에서 1의 개수를 세어주는 Integer.bitCount() 메서드도 있었다.
 */
class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        while (n > 0) {
            if ((n & 1) == 1) {
                count++;
            }
            n >>= 1;
        }
        return count;
    }
}

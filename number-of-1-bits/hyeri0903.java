class Solution {
    public int hammingWeight(int n) {
        /**
        1.문제: 이진수 변환 후 1의 개수 반환
        2. 2로 나누면서 나머지가 1일 경우 count+=1
         */
        int count = 0;
        //  while(n > 0) {
        //     if (n % 2 != 0) {
        //         count += 1;
        //     }
        //     n = n / 2;
        //  }

         while(n > 0) {
            if ((n & 1) == 1) {
                count += 1;
            }
            n >>= 1;
         }
        return count;
    }
}

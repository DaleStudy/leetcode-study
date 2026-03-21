import java.util.HashMap;

class Solution {
    // n & (n-1) -> 마지막 set bit 제거
    // n & -n -> 마지막 set bit 추출
    // i >> 1 -> 절반
    // i & 1 -> 마지막 bit
    // i & (i - 1) == 0 -> i는 2의 거듭제곱

    // Follow up: If this function is called many times, how would you optimize it?
    // I'll cache the results in a HashMap.
    // (Or I can use lookup table or DP)
    private HashMap<Integer, Integer> cache = new HashMap<>();

    public int hammingWeight(int n) {
        // simple in Java
        // return Integer.bitCount(n);

        if (cache.containsKey(n)) {
            return cache.get(n);
        }

        int buffer = n;
        int answer = 0;

        // 1. self thought solution
        // TC : O(log n)
        // SC : O(1)
        while (buffer > 0) {
            answer += buffer % 2;
            buffer = buffer / 2;
        }

        // 2. fancy solution from leetcode using bit computing
        // TC : O(log n)
        // SC : O(1)
        // while(buffer > 0){
        // if((buffer & 1) == 1){
        // answer++;
        // }
        // buffer = buffer >> 1;
        // }

        // 3. another fancy solution from ChatGPT
        // Brian Kernighan algorithm
        // TC : O(number of set bits)
        // SC : O(1)
        // while (buffer != 0) {
        // // 11 & 10 => 1 & 0 => 0
        // buffer = buffer & (buffer - 1); // AND with buffer and buffer -1 => remove
        // last set bit.
        // System.out.println(buffer);
        // answer++;
        // }

        // 4. using lookup table
        // int[] table = new int[256];
        // for (int i = 0; i < 256; i++) {
        // table[i] = (i & 1) + table[i >> 1];
        // }
        // answer = table[buffer & 0xff] +
        // table[(buffer >> 8) & 0xff] +
        // table[(buffer >> 16) & 0xff] +
        // table[(buffer >> 24) & 0xff];

        // 5. DP
        // int[] bits = new int[n + 1];
        // for (int i = 1; i <= n; i++) {
        // bits[i] = bits[i >> 1] + (i & 1);
        // }

        cache.put(n, answer);
        return answer;
    }
}

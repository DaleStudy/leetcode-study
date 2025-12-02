/*
Integer.toBinaryString() 메서드 기억하기
*/


import java.util.*;

class Solution {
    public int hammingWeight(int n) {
        String s = Integer.toBinaryString(n);
        int count = 0;

        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (c == 49) {
                count += 1;
            }
        }

        return count;
    }
}


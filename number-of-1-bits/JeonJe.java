import java.util.*;

// TC: O(1)
// SC: O(1)
class Solution {
    public int hammingWeight(int n) {
        int answer = 0;

        while (n != 0) {
            if ((n & 1) == 1) {
                answer++;
            }
            n = n >>> 1;
        }
        return answer;
    }
}

import java.util.*;

// TC: O(1)
// SC: O(1)
class Solution {
    public int reverseBits(int n) {
        int answer = 0;
        for (int i = 0; i < 32; i++) {
            int bitFlag = (n >> i) & 1;
            answer += (bitFlag << (31 - i));
        }
        return answer;
    }
}

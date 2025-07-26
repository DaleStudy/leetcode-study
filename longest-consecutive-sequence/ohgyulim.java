import java.util.*;

class Solution {
    /* 시간 복잡도: O(N)
    * - for 루프: O(N) O(N)
    *   - HashSet(add, contains): O(1)
    * 
    * 공간 복잡도: O(N), HashSet에 n개
    */ 
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int answer = 0;
        for (int num : set) {
            if (!set.contains(num - 1)) {
                int cur = num;
                int count = 1;
                while (set.contains(cur + 1)) {
                    cur += 1;
                    count += 1;
                }
                answer = Math.max(answer, count);
            }
        }

        return answer;
    }
}


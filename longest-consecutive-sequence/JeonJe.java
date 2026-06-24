import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0 || nums.length == 1) {
            return nums.length;
        }


        HashSet<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }

        int answer = 1;
        for (Integer cur : set) {
            if (set.contains(cur - 1)) {
                continue;
            }

            int right = cur;
            while (set.contains(right + 1)) {
                right++;
            }
            answer = Math.max(answer, right - cur + 1);
        }

        return answer;
    }
}

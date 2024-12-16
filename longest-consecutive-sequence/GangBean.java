import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        int maxLength = 0;
        for (int num: nums) {
            // 각 숫자에 대해 최초 값이 가능하면, 즉 num-1이 존재하지 않으면 최대 length 구하기
            if (set.contains(num - 1)) continue;
            int length = 1;
            int start = num;
            while (set.contains(start + 1)) {
                length++;
                start++;
            }
            maxLength = Math.max(length, maxLength);
        }

        return maxLength;
    }
}

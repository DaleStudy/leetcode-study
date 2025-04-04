
/**
 * 정렬되지 않은 정수 배열 nums가 주어질 때 가장 긴 연속적인 요소 배열의 길이를 반환
 * */
import java.util.Arrays;
public class Solution {

    public int longestConsecutive(int[] nums) {

        if (nums.length == 0) {
            return 0;
        }

        Arrays.sort(nums);

        int maxCnt = 1;
        int cnt = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                continue;
            }
            if (nums[i] + 1 == nums[i + 1]) {
                cnt++;
            } else {
                cnt = 1;
            }
            maxCnt = Math.max(maxCnt, cnt);
        }
        return maxCnt;
    }

}

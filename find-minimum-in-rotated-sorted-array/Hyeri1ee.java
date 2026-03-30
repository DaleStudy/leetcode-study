//맨뒤 요소 맨앞으로
import java.util.*;


class Solution {
    public int findMin(int[] nums) {
        Arrays.sort(nums);
        return nums[0];
    }
}


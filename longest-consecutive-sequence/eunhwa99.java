import java.util.Arrays;

// 시간 복잡도: O(nlogn) - 정렬
// 공간 복잡도: O(1)
class Solution{
    public int longestConsecutive(int[] nums){
        if(nums.length == 0) return 0;
        Arrays.sort(nums);
        int pre = nums[0];
        int max = 1;
        int count = 1;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] == pre + 1){
                count++;
                max = Math.max(max, count);
            } else if(nums[i] != pre){
                count = 1;
            }
            pre = nums[i];
        }
        return max;
    }
}

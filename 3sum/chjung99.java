// two pointer
// time: O(N^2)
// space: O(N)

class Solution {
    Set<List<Integer>> set = new HashSet<>();
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; i++){
            twoSum(nums, i);
        }

        return new ArrayList<>(set);
    }
    public void twoSum(int[] nums, int targetIdx){
        int left = 0;
        int right = nums.length - 1;

        while (left < right) {
            if (left == targetIdx){
                left ++;
                continue;
            }
            if (right == targetIdx){
                right--;
                continue;
            }
            if (nums[left] + nums[right] == -nums[targetIdx]) {
                if (nums[left] > nums[targetIdx]){
                    set.add(List.of(nums[targetIdx], nums[left], nums[right]));
                }
                else if (nums[targetIdx] > nums[right]){
                    set.add(List.of(nums[left],nums[right],nums[targetIdx]));
                } else{
                    set.add(List.of(nums[left], nums[targetIdx], nums[right]));
                }
                left++;
            } else if (nums[left] + nums[right] < -nums[targetIdx]){
                left ++;
            } else {
                right --;
            }
        }
    }
}



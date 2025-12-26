/**
	dp를 활용한 방식
	nums의 길이 -> N
	시간 복잡도 : O(N)
	공간 복잡도 : O(N)
*/
class Solution {
   public int lengthOfLIS(int[] nums) {
        int[] dp =new int[nums.length];
        for(int i = 0; i < dp.length; i++) {
            for(int j = 0; j < i; j++) {
                if(nums[i] > nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }
        return Arrays.stream(dp)
                    .max()
                    .getAsInt() + 1;
    }
}

/**
	이분탐색 활용한 방식
	nums의 길이 -> N
	시간 복잡도 : O(NlogN)
	공간 복잡도 : O(N)
*/
class Solution {
    public int[] list;
    public int lengthOfLIS(int[] nums) {
        int result = 0;
        list =new int[nums.length];
        Arrays.fill(list, Integer.MAX_VALUE);
        for(int i = 0; i < list.length; i++) {
            int idx = binarySearch(list, nums[i]);
            list[idx] = nums[i];
            result = Math.max(result, idx + 1);

        }
        return result;
    }

    public int binarySearch(int[] list, int target) {
        int start = 0;
        int end = list.length - 1;

        while(start <= end) {
            int mid = (start + end) / 2;
            if(list[mid] >= target) {
                end = mid - 1;
            } else {
                start = mid + 1;
            }
        }

        return start;
    }
}

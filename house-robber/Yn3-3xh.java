/*
[문제풀이]
(X) 주어진 nums 배열에서 index 홀수의 합과 짝수의 합을 비교해보자.
    class Solution {
        public int rob(int[] nums) {
            if (nums.length == 1) {
                return nums[0];
            }

            for (int i = 1; i <= nums.length; i++) {
                int beforeStepIndex = i - 2;
                if (beforeStepIndex >= 1) {
                    nums[i - 1] += nums[beforeStepIndex - 1];
                }
            }
            return Math.max(nums[nums.length - 1], nums[nums.length - 2]);
        }
    }
    >> 바로 옆이 아니어도 된다.

(O) 현재 num과 이전 num을 비교하여, 큰 값을 기준으로 더한다.
time: O(N), space: O(1)
    class Solution {
        public int rob(int[] nums) {
            int prevNum = 0;
            int sum = 0;
            for (int num : nums) {
                int temp = Math.max(sum, prevNum + num);
                prevNum = sum;
                sum = temp;
            }
            return sum;
        }
    }
    >> 공간복잡도 최적화 솔루션으로, dp 보다 직관적이지 않아, 메모리 사용이 제한되거나 입력 크기가 매우 클 때 사용하는 것이 좋을 듯

time: O(N), space: O(N)
    class Solution {
        public int rob(int[] nums) {
            if (nums.length == 1) {
                return nums[0];
            }

            int[] dp = new int[nums.length];
            dp[0] = nums[0];
            dp[1] = Math.max(nums[0], nums[1]);

            for (int i = 2; i < nums.length; i++) {
                dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
            }
            return dp[nums.length - 1];
        }
    }
    >> 공간복잡도는 좀 더 높지만, 직관적이다.
[회고]
개발은 혼자하는 것이 아니기도 하고, 디버깅하기 쉽게 직관적인 DP로 푸는게 좋지 않을까?..?
*/
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }
        return dp[nums.length - 1];
    }
}

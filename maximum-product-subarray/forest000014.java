/*
# Time Complexity: O(n)

# Space Complexity: O(1)

# Solution
1. array에 0이 존재하는 경우

(observation: 정답이 음수가 될 가능성이 있는가? Yes. 다만, 원소 개수가 1개이고, 그 원소가 음수인 경우에만 그렇다. 음수인 원소가 2개 이상인 경우는 subarray를 잘 선택하면 그 곱을 항상 0 이상으로 만들 수 있다. 즉, 원소 개수가 1개이고 음수인 경우만 예외 처리를 해주면, 그 외의 경우는 정답이 0이거나 양수이다.)

subarray에 0이 포함되는 순간 곱은 0이 되므로, 0보다 큰 곱을 찾기 위해서는 0을 제외하고 판단한다. 
즉, 0을 기준으로 slice해서, 각각의 segment만 독립적으로 검토하면 된다. (0으로 slice한 각 segment가 아래 2번 케이스로 환원된다.)

2. (sub)array에 0이 존재하지 않는 경우
음수의 개수에 따라 접근을 다르게 한다.

2-1. 짝수개
고민할 것 없이, 전체 subarray의 원소를 곱하면 그 subarray에서 얻을 수 있는 곱의 최대값이다.

2-2. 홀수개
subarray 양 끝에서 각각 출발하여 최초의 마이너스(즉 가장 바깥쪽의 마이너스)를 만날 때까지, 원소들을 누적해서 곱하며 이동.
두 값 중 절대값이 작은 쪽을 subarray에서 제외. 남은 부분의 곱을 구하면, 최대값이다.
*/

class Solution {
    public int maxProduct(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        int ans = 0;
        int start = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                continue;
            }

            if (i > 0) {
                int res = calculateMaxProduct(start, i - 1, nums);
                ans = Math.max(ans, res);
            }
            start = i + 1;
        }

        if (start <= nums.length - 1) {
            int res = calculateMaxProduct(start, nums.length - 1, nums);
            ans = Math.max(ans, res);
        }

        return ans;
    }

    private int calculateMaxProduct(int l, int r, int[] nums) {
        if (l == r) {
            return nums[l];
        }

        int minusCount = 0;
        int product = 1;
        for (int i = l; i <= r; i++) {
            if (nums[i] < 0) {
                minusCount++;
            }
            product *= nums[i];
        }

        if (minusCount % 2 == 0) {
            return product;
        } else {
            int leftProduct = 1;
            for (int i = l; i <= r; i++) {
                leftProduct *= nums[i];
                if (nums[i] < 0) {
                    break;
                }
            }

            int rightProduct = 1;
            for (int i = r; i >= l; i--) {
                rightProduct *= nums[i];
                if (nums[i] < 0) {
                    break;
                }
            }

            return product / Math.max(leftProduct, rightProduct);
        }
    }
}

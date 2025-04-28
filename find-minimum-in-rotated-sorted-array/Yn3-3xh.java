/**
[문제풀이]
- 왼쪽의 수 보다 오른쪽의 수가 작은 순간을 찾자.
- 가장 왼쪽의 수 보다 가장 오른쪽의 수가 크면 회전이 일어나지 않은 상태이므로, 첫번째가 최솟값이다.
- 풀이1
time: O(N), space: O(1);
    class Solution {
        public int findMin(int[] nums) {
            if (nums.length == 1) {
                return nums[0];
            }

            for (int i = 1; i < nums.length; i++) {
                if (nums[i - 1] > nums[i]) {
                    return nums[i];
                }
            }
            return nums[0];
        }
    }
- 풀이2 <이진탐색>
time: O(log N), space: O(1)

[회고]
이진탐색으로 푸는 능력이 부족한 것 같다.
 */

class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        if (nums[left] < nums[right]) {
            return nums[left];
        }

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] <= nums[right]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return nums[left];
    }
}



class Solution {
    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        // 0번째값이 length-1번재 값보다 작다면 rotate되지 않았음을 보장합니다.
        // 2,3,4,5,1  0번째 > length-1번째
        // 3,4,5,1,2  0번째 > length-1번째
        // 1,2,3,4,5  0번째 < length-1번째
        if (nums[right] >= nums[left]) return nums[0];

        while (left < right) {
            // 단순히 (left+right)/2 보다 범위 계산 오차가 없습니다.
            int mid = left + (right - left) / 2;

            // 중간값이 오른쪽값보다 크다면 왼쪽 포인터를 중간값+1로 증가합니다.
            if (nums[mid] > nums[right]) { // <= 와 동일
                left = mid + 1;
            } else {
                // 중간값보다 오른쪽값이 크다면 중간값이 최대 범위가 되어야 합니다.
                // 최소값이 mid일 가능성이 있기 때문이다.
                right = mid;
            }
        }
        return nums[left];
    }
}

// 처음에는 전형 이진 탐색으로서 left = mid+1, right = mid-1을 했으나 실패
// 하지만 최소 숫자는 무조건 left가 가리키는 값임.

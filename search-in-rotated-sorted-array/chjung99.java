class Solution {
    public int search(int[] nums, int target) {
        int leftSide = 0;
        int rightSide = nums.length - 1;
        int left = 0;
        int right = nums.length;
        int mid;

        if (nums.length == 1) {
            if (nums[0] == target) return 0;
            else return -1;
        }

        while (left + 1 < right) {
            mid = (int) (left + right) / 2;

            if (nums[mid]==target) {
                break;
            }
            else if (nums[mid] < target){ // 값이 증가해야함
                if (nums[mid] >= nums[leftSide]){ // 왼쪽 그룹에 속하는 지
                    left = mid;
                } else { // 오른쪽 그룹에 속하는 지
                    if (nums[rightSide] < target) {
                        right = mid;
                    } else {
                        left = mid;
                    }
                }
            } else{ // nums[mid] > target // 값이 감소해야함
                if (nums[mid] >= nums[leftSide]){ // 왼쪽 그룹에 속하는 지
                    if (nums[leftSide] <= target) {
                        right = mid;
                    } else {
                        left = mid;
                    }
                } else { // 오른쪽 그룹에 속하는 지
                    right = mid;
                }

            }
        }
        mid = (int)((left + right) / 2);
        if (nums[mid]==target) return mid;
        else return -1;
    }
}



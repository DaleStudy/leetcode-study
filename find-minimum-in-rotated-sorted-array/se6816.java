/**
    for문 순회를 통해 최소값 찾기
    nums의 길이 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(1)
 */
class Solution {
    public int findMin(int[] nums) {
        int result = Integer.MAX_VALUE;
        for(int num : nums) {
            result = Math.min(result, num);
        }
        return result;
    }
}

/**
    이분 탐색을 통해, 최소 요소를 구하는 방식
     nums의 길이 -> N
     시간 복잡도 : O(logN)
     공간 복잡도 : O(1)
*/
class Solution {
    public int findMin(int[] nums) {
        return nums[binarySearch(nums)];
    }

    public int binarySearch(int[] nums) {
        int start = 0;
        int end = nums.length -1;
        while(start < end) {
            int mid = (start + end) / 2;
            if(nums[mid] < nums[end]) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }
}


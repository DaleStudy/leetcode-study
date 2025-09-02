public class Geegong {

    /**
     * two pointer 사용
     * time complexity : o(log n)
     * space complexity : o(1)
     *
     * when nums are sorted array, binary search could be used in O(log n)
     * (rotating doesn't matter)
     * @param nums
     * @return
     */
    public int findMin(int[] nums) {
        int leftIndex = 0;
        int rightIndex = nums.length - 1;

        while(leftIndex < rightIndex) {
            int midIndex = leftIndex + ((rightIndex - leftIndex) / 2);

            if (nums[midIndex] > nums[rightIndex]) {
                leftIndex = midIndex + 1;
                // midIndex 에 +1 하는 이유는 midIndex 값은 이미 rightIndex 보다 크다고 판단이 되기에 최솟값이 될 수 없어
                // midIndex 의 값은 배제한다.
            } else if (nums[midIndex] < nums[rightIndex]) {
                rightIndex = midIndex - 1;
            } else if (nums[midIndex] == nums[rightIndex]) { // 두개 인덱스가 같아질 수가 있나?
                return nums[midIndex];
            }
        }

        return nums[leftIndex];
    }

}


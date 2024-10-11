class `find-minimum-in-rotated-sorted-array` {

    /**
     * TC: O(log N), SC: O(1)
     */
    fun findMin(nums: IntArray): Int {
        var (low, high) = 0 to nums.size - 1

        while (low + 1 < high) {
            val mid = (low + high) / 2
            if (nums[mid - 1] > nums[mid]) {
                return nums[mid]
            }
            if (nums[mid] < nums[high]) {
                high = mid
            }
            else {
                low = mid
            }
        }

        return min(nums[low], nums[high])
    }

    @Test
    fun `입력받은 정수 배열의 최소 원소를 반환한다`() {
        findMin(intArrayOf(4,5,6,7,0,1,2)) shouldBe 0
        findMin(intArrayOf(2,3,0,1)) shouldBe 0
        findMin(intArrayOf(2,3,1)) shouldBe 1
        findMin(intArrayOf(2,1,3)) shouldBe 1
        findMin(intArrayOf(2,3,4,5,1)) shouldBe 1
        findMin(intArrayOf(11,13,15,17)) shouldBe 11
    }
}

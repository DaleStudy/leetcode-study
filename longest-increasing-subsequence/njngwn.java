// time complexity: O(nlogn), n: nums.length (logn because of binary search)
// space complexity: O(n), n: nums.length
class Solution {
    public int lengthOfLIS(int[] nums) {
        ArrayList<Integer> incSeqList = new ArrayList<Integer>();   // dp
        incSeqList.add(nums[0]);

        for (int num : nums) {
            if (num > incSeqList.get(incSeqList.size()-1)) {
                // add element to incSeqLit
                incSeqList.add(num);
            } else {
                int idx = Collections.binarySearch(incSeqList, num);
                if (idx < 0) {  // idx returns -(insertedPos + 1)
                    int insertedIdx = -(idx + 1);
                    incSeqList.set(insertedIdx, num);
                }
            }
        }

        return incSeqList.size();
    }
}

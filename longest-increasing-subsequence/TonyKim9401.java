// TC: O(n log n)
// -> nums for loop O(n) + binarySearch O(log n)
// SC: O(n)
// -> ArrayList could have nums all elements
class Solution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> output = new ArrayList<>();

        for (int num : nums) {
            int start = 0;
            int end = output.size();
            while (start < end) {
                int mid = start + (end - start) / 2;
                if (output.get(mid) < num) start = mid + 1;
                else end = mid;
            }
            if (start == output.size()) output.add(num);
            else output.set(start, num);
        }
        return output.size();
    }
}

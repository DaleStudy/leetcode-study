class Solution {
    public int longestConsecutive(int[] nums) {
        int longest = 0;
        Set<Integer> set = Arrays.stream(nums)
                .boxed()
                .collect(Collectors.toSet());

        for (Integer i : set) {
            if (set.contains(i - 1)) continue;
            int length = 1;

            while (set.contains(i + 1)) {
                length++;
                i++;
            }
            longest = Math.max(longest, length);
        }
        return longest;
    }
}

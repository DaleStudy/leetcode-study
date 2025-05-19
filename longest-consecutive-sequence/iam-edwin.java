class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = Arrays.stream(nums)
            .boxed()
            .collect(Collectors.toSet());

        return set.stream()
            .map(num -> {
                if (set.contains(num - 1)) {
                    return 0;
                }
    
                int consecutiveLength = 1;
    
                while (set.contains(num + 1)) {
                    consecutiveLength += 1;
                    num += 1;
                }
    
                return consecutiveLength;
            })
            .mapToInt(num -> num)
            .max()
            .orElse(0);
    }
}

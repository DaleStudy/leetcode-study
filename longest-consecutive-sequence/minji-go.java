/**
 * <a href="https://leetcode.com/problems/longest-consecutive-sequence/">week01-4.longest-consecutive-sequence</a>
 * <li> Description: return the length of the longest consecutive elements sequence </li>
 * <li> Concept: Array, Hash Table, Union Find  </li>
 * <li> Time Complexity: O(n), Runtime: 60ms  </li>
 * <li> Space Complexity: O(n), Memory: 55.7MB </li>
 */

class Solution {
    private Set<Integer> set;

    public int longestConsecutive(int[] nums) {
        set = Arrays.stream(nums)
                .boxed()
                .collect(Collectors.toSet());

        return set.stream()
                .filter(num -> !set.contains(num-1))
                .map(this::calculateLength)
                .max(Integer::compareTo)
                .orElse(0);
    }

    public int calculateLength(int num) {
        return (int) IntStream.iterate(num, n->n+1)
                .takeWhile(set::contains)
                .count();
    }
}

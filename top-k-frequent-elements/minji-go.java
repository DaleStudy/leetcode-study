/**
 * <a href="https://leetcode.com/problems/top-k-frequent-elements/">week01-3.top-k-frequent-elements</a>
 * <li> Description: return the k most frequent elements   </li>
 * <li> Concept: Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect </li>
 * <li> Time Complexity: O(n log k), Runtime: 15ms     </li>
 * <li> Space Complexity: O(n), Memory: 49.4MB        </li>
 */

class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> map = Arrays.stream(nums)
                .boxed()
                .collect(Collectors.toMap(num -> num, num -> 1, (cnt, cnt2) -> cnt + 1));

        return map.entrySet().stream()
                .sorted(Map.Entry.comparingByValue(Collections.reverseOrder()))
                .limit(k)
                .map(Map.Entry::getKey)
                .mapToInt(Integer::intValue)
                .toArray();
    }
}

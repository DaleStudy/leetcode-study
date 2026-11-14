class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /*
        Approach
        1. using map, key -> num, value -> count
        2. sort
        */

        Map<Integer, Integer> count = new HashMap<>();
        for (int num: nums) { // O(n)
            count.put(num, count.getOrDefault(num,0)+1);
        }

        return count.entrySet().stream()
            .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder())) // O(nlogn)
            .map(Map.Entry::getKey)
            .limit(k)
            .mapToInt(Integer::intValue)
            .toArray();
        /*
        Complexity
        - time: O(nlogn) // sort
        - space: O(n)   // declare map?
        */
    }
}

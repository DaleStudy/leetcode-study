class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        /*
        Approach 1
        1. using map, key -> num, value -> count
        2. sort
        */

        Map<Integer, Integer> count = new HashMap<>();
        for (int num: nums) { // O(n)
            count.put(num, count.getOrDefault(num,0)+1);
        }

        // return count.entrySet().stream()
        //     .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
        //     .map(Map.Entry::getKey)
        //     .limit(k)
        //     .mapToInt(Integer::intValue)
        //     .toArray();
        // /*
        // Complexity
        // - time: O(nlogn) // sort
        // - space: O(n)   // declare map?
        // */


       /*
        Approach 2
        1. using map, key -> num, value -> count
        2. Initialize a 2D dynamic array (buckets) and group numbers by their frequency
        */
        List<List<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i <= nums.length; i++) {
            buckets.add(new ArrayList<>());
        }
        for (int key: count.keySet()) {
            buckets.get(count.get(key)).add(key);
        }

        int[] result = new int[k];
        int idx = 0;
        for (int i = buckets.size()-1;i>=0;i--) {
            for (int j = 0; j < buckets.get(i).size(); j++) {
                if (idx<k) {
                    result[idx] = buckets.get(i).get(j);
                    idx++;
                } else {
                    return result;
                }

            }
        }

        return result;
        /**
        Complexity
        - time: O(n) -> o(n) + o(n) + o (n+1+ n) -> o(4n+1)
        - space: O(n) -> dynamic 2d array (buckets)
         */
    }
}

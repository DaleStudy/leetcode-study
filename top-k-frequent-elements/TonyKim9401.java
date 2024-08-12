class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // declare hashmap 
        // key: each element, value: appered count
        Map<Integer, Integer> map = new HashMap<>();

        // if map contains the element, increase its value by one.
        // else put the element and 1 for initializing
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.getOrDefault(num, 0) + 1);
            } else {
                map.put(num, 1);
            }
        }

        // keyList only has key values of the hashmap
        // using their value count sort keys by descending order
        List<Integer> keyList = new ArrayList<>(map.keySet());
        Collections.sort(keyList, (o1, o2) -> map.get(o2).compareTo(map.get(o1)));


        int[] output = new int[k];
        int idx = 0;

        // retreive keys k times and set output
        while (idx < k) output[idx] = keyList.get(idx++);

        return output;
    }
}
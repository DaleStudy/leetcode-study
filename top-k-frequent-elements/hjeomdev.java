class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            int current = map.getOrDefault(num, 0);
            map.put(num, current + 1);
        }

        List<Integer> keySet = new ArrayList<>(map.keySet());
        keySet.sort((o1, o2) -> map.get(o2).compareTo(map.get(o1)));

        return keySet.subList(0, k)
                .stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
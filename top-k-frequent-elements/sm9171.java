class Solution {
    public static int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        List<Integer> list = hashMap.entrySet().stream()
                .sorted(Map.Entry.<Integer, Integer>comparingByValue().reversed())
                .limit(k)
                .map(Map.Entry::getKey)
                .toList();

        int[] result = list.stream()
                .mapToInt(Integer::intValue)
                .toArray();

        return result;
    }
}

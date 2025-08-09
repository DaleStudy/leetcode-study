class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        // value 를 기준으로 정렬
        List<Map.Entry<Integer, Integer>> entrySet = new ArrayList<>(map.entrySet());
        entrySet.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            
            result[i] =  entrySet.get(i).getKey();
        }
        return result;
    }
}

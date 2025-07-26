/*
time complexity : O(nlogn)
space complexity : O(n)
*/
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> numMap = new HashMap<>();
        for (int num:nums) {
            if (numMap.containsKey(num)) {
                int value = numMap.get(num);
                numMap.put(num, value + 1);
            } else {
                numMap.put(num, 1);
            }
        }
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(numMap.entrySet());
        entryList.sort((a, b) -> b.getValue() - a.getValue());
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = entryList.get(i).getKey();
        }
        return result;
    }
}

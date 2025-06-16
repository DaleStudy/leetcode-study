
class Solution {
    public int missingNumber(int[] nums) {

        int len = nums.length;
        Map<Integer, Boolean> nMap = new HashMap<>();

        for (int i = 0; i <= len; i++) {
            nMap.put(i, true);
        }

        for (int anInt : nums) {
            nMap.remove(anInt);
        }

        List<Integer> keyList = new ArrayList<>(nMap.keySet());

        return keyList.get(0);
    }
}

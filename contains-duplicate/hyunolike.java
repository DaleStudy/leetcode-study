class Solution {
    public boolean containsDuplicate(int[] nums) {
        // 중복 체크
        // 각 요소 순환

        // 1. 배열 순환
        // 2. 2 이상 true 체크

        // 자료구조 Map 사용
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            //System.out.println(num);
            if (map.containsKey(num)) {
                return true;
            }

            map.put(Integer.valueOf(num), Integer.valueOf(num));
        }

        return false;
    }
}
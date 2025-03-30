import java.util.HashSet;
import java.util.Set;

class Solution {

    /** 217. 중복된 수
      * 정수 배열 nums가 주어졌을 때 배열 요소 중 한 개 이상이 두 번 이상 중복되어
      * 나타는 경우 true를, 모든 배열의 요소가 고유한 경우 false를 반환
      */
    public boolean containsDuplicate(int[] nums) {

        Set<Integer> distincts = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            distincts.add(nums[i]);
        }

        return distincts.size() != nums.length;
    }
}


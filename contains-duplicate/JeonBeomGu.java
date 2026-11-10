import java.util.HashSet;
import java.util.Set;

/**
 * 시간 복잡도: O(n) - nums 배열 길이인 n번 만큼 반복문이 반복될 수 있음
 * 공간 복잡도: O(n) - set에 데이터를 저장할 때 nums 배열 길이인 n개의 공간만큼 추가 공간이 필요
 */
public class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                return true;
            } else {
                set.add(nums[i]);
            }
        }

        return false;
    }
}

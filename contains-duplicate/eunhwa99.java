import java.util.HashSet;

// 공간 복잡도; O(n)
// 시간 복잡도: O(1)
class Solution {
    public boolean containsDuplicate(int[] nums) {
         HashSet<Integer> visited = new HashSet<>();
        for (int num : nums) {
            if (!visited.add(num)) {
                return true;
            }
        }
        return false;
    }
}

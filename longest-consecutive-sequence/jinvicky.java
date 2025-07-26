import java.util.HashSet;
import java.util.Set;

// 연속적인 숫자의 길이를 구하는 것이기 때문에 이전, 다음 수가 집합의 일부인지를 파악해야 한다.
// map, set 자료구조를 사용하면 조회 성능을 O(1)로 높일 수 있다.
// 어려웠던 점은 연속적인 숫자의 start가 되냐 여부 조건을 떠올리는 것이었다. while문이 약해서 length++하는 로직이 힘들었다.
// 문제의 조건은 배열 내에서의 연속적인 숫자의 길이이기 때문에 while을 사용해도 성능 이슈 걱정할 필요가 없었다.
class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int n : nums) {
            set.add(n);
        }

        int maxLength = 0;

        for (int n : nums) {
            if (!set.contains(n - 1)) { // 내 이전 숫자가 집합에 없다 == 내가 최소 숫자다.
                int length = 1;

                while (set.contains(n + length)) {
                    length++;
                }

                maxLength = Math.max(length, maxLength);
            }
        }

        return maxLength;
    }
}

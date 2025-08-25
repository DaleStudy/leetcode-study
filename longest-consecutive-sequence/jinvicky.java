import java.util.HashSet;
import java.util.Set;

/**
 * 왜 set을 썼을까? 내가 원하는 "특정 조건"을 제시했을 때 그 숫자를 O(1)으로 조회할 수 있기 때문이다.
 * set이 줄 것을 알기에 나는 조건을 설계하는 데만 집중한다.
 * 1. 내가 포함된 연속된 시퀀스가 있는가? -> set.contains(n-1)
 * 2. 내가 새로운 시퀀스의 start인가? -> !set.contains(n-1)
 * <p>
 * 여기서 가장 긴 길이를 구한다 == Math.max(기존 최대길이, 현재 계산한 최대길이) -> 자동으로 Math.max()가 떠오른다.
 * 현재 최대길이는 본인을 포함한 1부터 시작한다.
 * [길이를 계산할 때 항상 해야 할까???] -> 아니다!
 * 왜? 이미 내가 포함된 연속된 시퀀스는 maxLength를 비교하는 과정을 거쳤는데 굳이 또?
 * <p>
 * 배움: 일단 계산을 떠올린다. -> 그리고 그 계산을 언제(if) 수행할 것인지 조건을 설정한다. (항상 해도 되는가? 중복되지는 않는가?)
 * <p>
 * [성능에 대한 잘못된 생각]
 * O(n)이라면 꼭 for문 1번으로 해결해야 한다는 잘못된 생각을 갖고 있었다.
 * 첫 번째 루프가 O(n), 두 번째 루프가 O(n)이고, 두 개를 합치면 O(n + n)입니다.
 * 시간 복잡도 계산에서 상수 계수는 무시되므로 결국 O(n)으로 표기한다.
 * <p>
 * [후기]
 * 처음에는 어 기존이랑... 지금이랑 별도 배열로 체크? 그런데 배열의 개수가 어디까지 늘어나지...?
 * 항상 기억할 점은 최대 길이, 최소 길이와 같은 문제는 결과가 중요하지 어느 숫자로 이루어져있는지 알 필요가 없다.
 */
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

/**
 * 1 .문제 정의
 *  배열이 주어지면, 배열에 포함된 정수가 중복이 없다면 fasle, 적어도 1회 이상 중복이 있다면 true를 반환해야한다.
 *  배열의 크기는?
 *   - 1 <= length <= 100000
 * 2. naive algorithm 도출
 *   - 배열을 탐색하면서 Set자료구조에 넣는다. 이때 Set에 넣으려는 값이 이미 포함되어있는지를 확인합니다.. true를 반환.
 *   - 배열 전체를 탐색했는데 포함여부에서 걸리지 않으면 false를 반환
 * 3. 시간&공간복잡도 분석
 * - 배열의 길이가 N이면 O(N)의 시간 복잡도
 * 4. 코드작성
 */
import java.util.*;
public class sangyyypark {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            int value = nums[i];
            if(set.contains(value)) {
                return true;
            }
            set.add(value);
        }
        return false;
    }
}


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

/**
 * 1 .문제 정의
 *  배열에서 동일한 숫자를 사용하지 않고 두개의 숫자를 선택해서 합이 target이 나오는지 판별해야 하는 문제
 *  - 배열의 길이는?
 *    - 2 <= length <= 10000 라고 가정합니다.
 *  - target을 만드는 경우가 여러개가 있다면?
 *    - 오직 하나의 경우만 있다고 가정합니다.
 * 2. naive algorithm 도출
 *  - 투포인터 알고리즘을 사용해서 구현
 *      - left,right를 각각 선정합니다.
 *      - left와 right가 같으면 합을 구하지 않고 Right를 1칸 전진합니다.
 *      - left와 right의 합을 구해서 target이 아니라면 right를 1칸 전진합니다.
 *      - right가 마지막에 도달했는데도 target이 아니라면 left를 1칸 전진합니다.
 *      - 위 과정을 반복합니다.
 * 3. 시간&공간복잡도 분석
 *   - 투포인터 알고리즘의 시간복잡도는 O(N^2)
 * 4. 코드작성
 */
public class sangyyypark {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = 1;
        int [] answer = new int [2];
        while(left < nums.length && right < nums.length) {
            int a = nums[left];
            int b = nums[right];
            if(target == a + b) {
                answer[0] = left;
                answer[1] = right;
                break;
            }


            if(right >= nums.length -1) {
                left++;
                right = left+1;
            }
            else {
                right++;
            }
        }
        return answer;
    }
}


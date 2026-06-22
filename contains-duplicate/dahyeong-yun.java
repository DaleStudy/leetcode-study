/**
 * [문제 분석 및 풀이]
 * 1. 시간복잡도 : N이 $10^5$ 까지 이므로 $O(N^2)$은 시간초과 가능성이 높음(1억번 연산 기준). O(N logn N) 이하 알고리즘을 고려해야 함.
 * 2. 제약 사항
 * - 자료형 제약 : 각 인덱스의 값이 +-10억 이므로 `int`로 처리 가능.
 * 3. 풀이 아이디어 : 정렬해서 원소 비교
 * - 중복 값이 있는지 아는 방법은 직관적으로는, 정렬했을 때 바로 다음 인덱스의 숫자와 같은 수가 있는지로 판별할 수 있음.
 * - Arrays.sort 는 O(N * log N) 이므로 충분히 가능한 시간 복잡도로 보임.
 * - 시공간복잡도 : Arrays.sort 정렬에 의해 시간복잡도는 O(N log N) 공간복잡도는 O(1) 이라고 볼 수 있음.
 */
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        
        int before = Integer.MAX_VALUE; // 문제 제약 상 해당 값이 할당되는 경우가 없어 중복 판단에 문제 없음.
        for(int num : nums) {
            if(before == num) return true;
            before = num;
        }
        return false;
    }
}

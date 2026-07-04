/**
 * 0. 풀이 개요
 *   - 시간복잡도 : O(n)
 *   - 공간복잡도 : O(n)
 */
class Solution {
    /**
     * 1. 풀이 과정
     * 1.1 이해
     *   - 각 배열의 원소가 본인을 제외한 모든 것이 곱해진 상태를 출력하면 됨.
     * 1.2 제약
     *   - n이 2부터 10^5까지 임. 배열을 순회하는 경우 n^2은 어려워 보임(10^8 기준). 따라서 n log n 이하가 필요
     * 1.3 아이디어
     *   - 사실 문제를 몇번 풀었어서 외워져 버림
     *   - 시각적으로 보이자면 2개의 배열을 활용하는 셈
     *   - | 배열 원소를 변수로 치환    | a  | b          | c          | d            |
     *     | prefix 의 상태         | 1   | 1 * a = a | a * b = ab | ab * c = abc |
     *     | suffix 의 상태         | bcd | cd        | d          | 1            |
     *     | prefix * suffix      | bcd | acd        | abd       |   abc        |
     *   - 시간복잡도는 n 번씩 두번 순회 하므로 2n 번 순회로 O(n)이 됨.
     *   - 공간복잡도는 n 크기 만큼의 배열을 추가로 생성하므로 O(n)이 됨.
     */
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int suffix = 1;

        int len = nums.length;
        int[] answer = new int[len];

        answer[0] = 1;
        for(int i = 1; i < len; i++) {
            answer[i] = prefix * nums[i-1]; 
            prefix *= nums[i-1];
        }

        for(int i = len-1; i >= 0; i--) {       
            answer[i] = answer[i] * suffix;
            suffix *= nums[i];
        }

        return answer;
    }
}

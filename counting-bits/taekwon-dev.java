/**
 *  공간 복잡도: O(N)
 *  시간 복잡도: O(N)
 *      - 만약 1 ~ N 까지 각 수에 대해서 이진수로 변환한 뒤 1의 개수를 카운트 했다면? - O(NlogN)
 *  Note:
 *   - a >> b: a 의 이진 표현을 오픈쪽으로 b 비트만큼 이동
 *   - i >> 1: a 의 이진 표현에서 가장 오픈쪽 하나가 잘림 (i는 양수 범위를 가지므로, 왼쪽은 0으로 채워짐)
 *   - a & b: AND 연산
 *   - i & 1: 이전 결과 값이 메모되어 있으므로, 내가 궁금한 것 가장 마지막 자리 수 값이 1인지 여부.
 */
class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            result[i] = result[i >> 1] + (i & 1);
        }
        return result;
    }
}

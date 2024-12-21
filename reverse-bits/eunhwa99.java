// 풀이방법
// n의 경우 끝에서부터 비트연산을 해야 하므로 가장 오른쪽부터 시작해야 함
// 이는 n과 1을 AND 연산하고, n을 오른쪽으로 미루면서 수행하면 된다. (n >> 1)
// 최종 결과를 위한 값은 result에 저장할 예정이다. result의 경우, n과 반대로 왼쪽으로 한 칸씩 미루면서 n의 비트를 삽입해줘야 함 (OR 연산)

// 시간 복잡도 (숫자의 비트 수 만큼 필요) -> O(N) (N: 숫자 n의 비트 수, 문제에서는 32로 고정)
// 공간 복잡도: (result 변수 크기)
public class Solution {

    public int reverseBits(int n) {
        int result = 0;
        for (int i = 0; i < 32; i++) {
            result = result << 1;
            result |= (n & 1);
            n = n >> 1;
        }
        return result;
    }
}


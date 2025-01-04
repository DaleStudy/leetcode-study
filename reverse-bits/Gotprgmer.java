// 처음 문제를 봤을때는 이해가 잘 가지 않았지만,
// 비트들을 뒤집으라는 설명으로 풀었던 것 같다.
// Integer.reverse() 메소드를 사용하여 풀었다.
// 지피티의 도움으로 Integer.reverse()를 사용하라는 힌트를 얻었다.
// 찾아보니 reverse(N)는 N을 2의 보수 비트로 바꾸고 그것을 뒤집는 방식이었다.
// 시간복잡도 : O(1) -> Integer가 32비트 고정이라서 O(1)
// 공간복잡도 : O(1) -> 32비트 고정
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        return Integer.reverse(n);
    }
}

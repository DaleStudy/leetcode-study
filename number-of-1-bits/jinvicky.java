class Solution {
    // [sol1] 반복문을 사용하면서 ((n>>i) & 1) == 1를 만족하는 개수를 구한다.
    public int hammingWeight(int n) {
        int answer = 0;
        for(int i = 0; i < 32; i++) {
            // >> 연산자를 이용하여 값을 오른쪽으로 bitwise 연산을 한다.
            if(((n>>i) & 1) == 1) {
                answer+=1;
            }
        }
        return answer;
    }

    // [sol2] 자바를 사용한다면 1개의 메서드, 1줄의 코드로 해결할 수 있다.
    public int hammingWeight2 (int n) {
        return Integer.bitCount(n);
    }
}

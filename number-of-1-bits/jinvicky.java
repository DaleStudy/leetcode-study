class Solution {
    // [sol1] 반복문을 사용하면서 ((n>>i) & 1) == 1를 만족하는 개수를 구한다.
    // n을 변경하지 않지만 [sol1-1]보다 느리다.
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

    // [sol1-1] n 값이 변경되면서 [sol1]보다 성능이 개선된다.
    public int hammingWeight1_1(int n) {
        int answer = 0;
        for (int i = 0; i < 32; i++) {
            answer += (n & 1);
            n >>>= 1;
        }
        return answer;
    }

    // [sol2] 자바를 사용한다면 1개의 메서드, 1줄의 코드로 해결할 수 있다.
    public int hammingWeight2 (int n) {
        return Integer.bitCount(n);
    }

    // [sol3] 1의 개수만큼만 반복한다.
    // 예) n = 1011 -> 1000 -> 0000 종료
    public int hammingWeight3(int n) {
        int answer = 0;
        while (n != 0) {
            n &= (n - 1); // 가장 오른쪽 1 비트를 0으로 만듦
            answer++;
        }
        return answer;
    }
}

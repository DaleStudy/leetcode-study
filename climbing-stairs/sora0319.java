// 공간 복잡도를 줄인 2번째 버전
class Solution {
    public int climbStairs(int n) {
        int back = 1;
        int front = 2;
        int target = 0;

        if (n == 1) return back;
        if (n == 2) return front;
        
        for(int i = 1; i < n-1; i++){
            target = front + back;
            back = front;
            front = target;
        }

        return target;
    }
}


// 초기 버전
class Solution {
    public int climbStairs(int n) {
        int[] stairs = new int[n+1];

        stairs[0] = 1;
        stairs[1] = 1;

        for(int i = 2; i <= n; i++){
            stairs[i] = stairs[i-1] + stairs[i-2];
        }
        return stairs[n];
    }
}

// 1 : 1
// 2 : [1] + 1, 2                           1+1 2  2개
// 3 : [2-1] + 1, [2-2] + 1, [1] + 2        1+1+1  2+1  1+2  3개
// 4 : [3-1] + 1, [3-2] + 1, [3-3] + 1      1+1+1+1  2+1+1   1+2+1  1+1+2  2+2  5개
// 5 :                                      1+1+1+1+1 2+1+1+1  1+2+1+1  1+1+2+1  1+1+1+2  2+2+1  2+1+2  1+2+2  8개


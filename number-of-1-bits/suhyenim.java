/* [5th/week03] 191. Number of 1 Bits

1. 문제 요약
링크: https://leetcode.com/problems/number-of-1-bits/description/
주어진 수를 이진수로 만들었을 때, 1의 개수 반환

2. 문제 풀이
제출1: 2로 나눈 나머지로 배열 만들고 -> 해당 배열에서 1의 개수 계산해서 반환
성공: 시간 복잡도는 O(logn), 공간 복잡도는 O(logn)
=> Time: 1 ms (16.28%), Space: 41.3 MB (7.99%)

class Solution {
    public int hammingWeight(int n) {
        List<Integer> rr = new ArrayList<>();
        while (n > 0) {
            int q = n / 2;
            int r = n % 2;
            rr.add(r);
            n = q;
        }
        int count = 0;
        for (int i = 0; i < rr.size(); i++) {
            if (rr.get(i) == 1) {
                count++;
            }
        }
        return count;
    }
}

*/

class Solution {
    public int hammingWeight(int n) {
        List<Integer> rr = new ArrayList<>();
        while (n > 0) {
            int q = n / 2;
            int r = n % 2;
            rr.add(r);
            n = q;
        }
        int count = 0;
        for (int i = 0; i < rr.size(); i++) {
            if (rr.get(i) == 1) {
                count++;
            }
        }
        return count;
    }
}

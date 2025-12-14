/*
1. 문제이해
배열의 숫자들 중 2개의 수를 구해서 가장 많이 담을 수 있는 물의 양을 구한다
이때 두 수중 작은 수를 기준으로 작은수 * 배열간의 거리 = 물의 양 으로 계산된다.

2. 예외케이스

3. 알고리즘
투포인터

4. 구현
두개의 포인터를 양쪽에 두고 최대값을 구하는 것이므로 두개의 포인터중 작은 값을 가지는 포인터를 반대방향으로 이동시킨다.
왜냐하면 큰 값을 가지는 포인터를 이동시켜버리면 그 다음 물의 양은 이전보다 클 수 없기 때문이다.

*/

import java.util.*;

class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int s = 0;
        int e = height.length - 1;

        while (s < e) {
            // 물의 양
            int area = (e - s) * Math.min(height[s], height[e]);
            maxArea = Math.max(area, maxArea);
            // 포인터 이동
            if (height[s] > height[e]) {
                e -= 1;
            } else {
                s += 1;
            }
        }

        return maxArea;
    }
}

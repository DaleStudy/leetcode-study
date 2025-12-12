/*
1. 문제 이해
입력받은 글자에 대해 뒤집어도 동일한 글자인지 아닌지를 판단

2. 예외 케이스
빈 문자열, 글자가 아닌 다른 내용일 경우 제거

3. 알고리즘
단순 루프

4. 구현

글자를 입력받고 글자가 아닌 내용에 대해서는 필터링한다
전체 길이를 구하고 2포인터로 왼쪽, 오른쪽을 서로 줄여가면서
같거나 교차할때 종료

다른 부분이 있으면 false 반환, 모두 통과하면 true 반환

빈 값일경우 바로 true


*/

import java.util.*;

class Solution {
    public boolean isPalindrome(String s) {
        String result = s.replaceAll("[^a-zA-Z0-9]", "");
        result = result.toLowerCase();

        int len = result.length();
        int left = 0;
        int right = len - 1;

        while (left < right) {
            char leftS = result.charAt(left);
            char rightS = result.charAt(right);

            if (leftS != rightS) {
                return false;
            }

            left += 1;
            right -= 1;
        }

        return true;
    }
}


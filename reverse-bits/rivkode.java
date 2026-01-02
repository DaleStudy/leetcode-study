/*

1. 문제이해
전달받은 int 를 binary bit 로 변환한다
변환한 값을 reverse 뒤집어서 다시 int로 변환한다 

2. 알고리즘
.toBinaryString() 과 .toUnsignedInt() 메서드를 활용한다

3. 예외
n 값은 sign 이므로 최대 21억까지 표현이 가능하다
n은 0보다 크므로 항상 첫번째 bit값은 0이다


4. 구현

전달받은 n을 bit로 변환
변환한 string을 stack 을 사용해서 push peek 하여 reverse
변환한 bit 값을 다시 int로 변환

처음에는 stack을 사용하려 했으나 최대 bit 수가 제한적 약 30개 이므로
매번 String을 생성하거나 StringBuilder를 사용해도 될 것 같다는 생각
굳이 자료구조를 만들어서 사용할 필요가 있을까 ?

toBinaryString() 을 하면 32칸을 채우지 못할 수 있으므로 마지막에 이 빈 0 에 대한 처리를 해줘야 한다
그래야 뒤집었을때 정상 결과 나옴

*/

import java.util.*;

class Solution {
    public int reverseBits(int n) {
        String bit = Integer.toBinaryString(n);
        StringBuilder sb = new StringBuilder();
        
        for (int i=bit.length() - 1; i>=0; i--) {
            System.out.println(i);
            char c = bit.charAt(i);
            int temp = c - '0';
            sb.append(String.valueOf(temp));
        }

        int size = bit.length();
        int leadingZero = 32 - size;
        for (int i=0; i<leadingZero; i++)
            sb.append("0");
        System.out.println(sb.toString());

        int decimalValue = Integer.parseInt(sb.toString(), 2);

        return decimalValue;
    }
}
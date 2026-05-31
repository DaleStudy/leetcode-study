/*
1. 문제 이해
n 을 입력받았을때 n+1 배열의 길이에서 각 인덱스 i 위치에 i 를 이진수로 전환했을때의 1의 개수를 입력한 배열을 반환

2. 구현
for 문을 돌면서 이진수를 변환하여 1의 개수를 카운팅한 값을 넣어준다
bitCount() 메서드를 사용할 수 있다.

*/

import java.util.*;

class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n+1];

        for (int i=0; i<n+1; i++) {
            int count = Integer.bitCount(i);
            arr[i] = count;
        }

        return arr;
    }
}

/*
입력받은 n에 대해 toBinaryString() 을 사용하여 binaryString 값을 알아낸뒤 charAt()으로 각 인덱스별 접근하여 1의 개수를 찾아내는 방식이다.
 */

// class Solution {
//     public int[] countBits(int n) {
//         int[] answer = new int[n + 1];
//         for (int i=0; i<n+1; i++) {
//             String bit = Integer.toBinaryString(i);
//             System.out.println(bit);
//             int cnt = 0;
//             for (int j=0; j < bit.length(); j++) {
//                 char c = bit.charAt(j);
//                 int num = c-'0';
//                 if (num == 1) {
//                     cnt += 1;
//                 }
//             }

//             answer[i] = cnt;
//         }

//         return answer;
//     }
// }



/*
입력받은 n에 대해 toBinaryString() 을 사용하여 binaryString 값을 알아낸뒤 charAt()으로 각 인덱스별 접근하여 1의 개수를 찾아내는 방식이다.
 */

class Solution {
    public int[] countBits(int n) {
        int[] answer = new int[n + 1];
        for (int i=0; i<n+1; i++) {
            String bit = Integer.toBinaryString(i);
            System.out.println(bit);
            int cnt = 0;
            for (int j=0; j < bit.length(); j++) {
                char c = bit.charAt(j);
                int num = c-'0';
                if (num == 1) {
                    cnt += 1;
                }
            }

            answer[i] = cnt;
        }

        return answer;
    }
}



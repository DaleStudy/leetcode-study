
/*
이전 풀이
class Solution {
    public int[] countBits(int n) {
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i <= n; i++) {
            int result = i;
            int cnt = 0;

            while(result > 0) {
                cnt += result%2;
                result /= 2;
            }

            list.add(cnt);
        }
        int[] ans = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            ans[i] = list.get(i);
        }
        return ans;
    }
}
*/
/*
시간 복잡도: O(n log n)
공간 복잡도: O(n)
 */
class Solution {
    public int[] countBits(int n) {
        // 0부터 n까지의 이진수를 만든다.
        // 이진수로 변환된 수에서 1의 갯수를 카운팅한다.
        // 0부터 n까지 1의 갯수를 카운팅한 것을 배열로 만들어 반환한다. 이때 배열의 길이는 n+1.
        int[] result = new int[n+1];
        
        for (int i = 0; i <= n; i++) {
            int num = divideTwo(i, 0);
            result[i] = num;
        }
        return result;
    }

    private int divideTwo(int n, int remainderCnt) {
        int divideNum = n/2;
        int remainder = n%2;

        int calcualteReminderNum = remainder + remainderCnt;
        if (divideNum == 0) return calcualteReminderNum;

        return divideTwo(divideNum, calcualteReminderNum);
    }
}

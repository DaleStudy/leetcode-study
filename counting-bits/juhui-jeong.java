

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

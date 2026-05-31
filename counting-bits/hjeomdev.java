class Solution {
    public int[] countBits(int n) {
        // 0 ~ n 까지 2진수를 구하고, 그 수의 모든 자릿값의 합을 구해야함

        int[] result = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            String binaryString = Integer.toBinaryString(i);
            int sum = 0;
            for (int j = 0 ; j < binaryString.length(); j++) {
                sum += binaryString.charAt(j) - '0';
            }
            result[i] = sum;
        }

        return result;
    }
}

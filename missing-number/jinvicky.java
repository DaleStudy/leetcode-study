class Solution {
    /**
     * 처음에는 set 자료구조를 동원해서 꼭 빠진 숫자를 찾겠다고 다짐했으나,
     * 생각해보니 단순히 범위가 0부터 nums.length까지의 연속된 시퀀스라면
     * 그냥 0부터 n까지 더했을 때의 원래 예상값에서 현재 nums의 합계를 빼면 되는 것이다.
     *
     * 최댓값, 최솟값을 구할때와 비슷하게 굳이 내용 안을 다 찾으려고 형식 자료구조에 얽매이지 않아도 된다.
     */
    public int missingNumber(int[] nums) {
        int expected = 0; // 0부터 n까지 더한 숫자의 합계
        int input = 0; //nums가 준 숫자들의 합계

        for (int n : nums) {
            input += n;
        }

        for (int i = 0; i <= nums.length; i++) {
            expected += i;
        }
//        System.out.println(expected + " and " + input);

        return expected - input;
    }
}
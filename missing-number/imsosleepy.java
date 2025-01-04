// GPT의 도움을 받은 결과, 수학적으로 접근하면 된다.
// 모든 값은 유니크하고 nums 배열 사이즈인 n을 지켜주기 때문에 가능한 결과
class Solution {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int expected = n * (n + 1) / 2;
        int actual = 0;
        for (int num : nums) {
            actual += num;
        }
        return expected - actual;
    }
}

// 시간복잡도는 O(N)으로 떨어진다.
// 공간복잡도가 nums 배열 사이즈에 종속되서 O(N)이다. 
// Accepted가 되지만, 다른 방법을 찾아봐야함
class Solution {
    public int missingNumber(int[] nums) {
        boolean[] existCheck = new boolean[nums.length + 1];

        for (int num : nums) {
            existCheck[num] = true;
        }

        for (int i = 0; i < existCheck.length; i++) {
            if (!existCheck[i]) {
                return i;
            }
        }

        return 0;
    }
}

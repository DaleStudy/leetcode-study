// 풀이
// 현재 인덱스가 i 일 때, 문제에서 구하고자 하는 값은 아래와 같다.
// 나의 왼쪽(i-1)부터 처음까지의 곱 * 나의 오른쪽(i+1)부터 끝까지의 곱
// leftProduct[i-1] = 왼쪽(i-1)부터 처음까지의 곱
// rightProduct[i+1] = 오른쪽(i+1)부터 끝까지의 곱
// leftProduct는 처음부터 i까지 순회하면서 구하면 된다. leftProduct[i] = leftProduct[i-1] * (나 자신 = nums[i])
// rightProduct는 끝부터 시작해서 i까지 순회하면서 구하면 된다. rightProduct[i] = rightProduct[i+1] * (나 자신 = nums[i])


// DP 를 사용하면 시간 복잡도는 O(N)
// 공간 복잡도는 2개의 배열이 필요하고, 답으로 보낼 배열까지 해서 O(3*N) = O(N)

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] leftProduct = new int[len];
        int[] rightProduct = new int[len];

        leftProduct[0] = nums[0];
        rightProduct[len - 1] = nums[len - 1];
        for (int i = 1; i < len; ++i) {
            leftProduct[i] = leftProduct[i - 1] * nums[i];
            rightProduct[len - i - 1] = rightProduct[len - i] * nums[len - i - 1];
        }

        int[] result = new int[len];
        result[0] = rightProduct[1];
        result[len - 1] = leftProduct[len - 2];
        for (int i = 1; i < len - 1; ++i) {
            result[i] = leftProduct[i - 1] * rightProduct[i + 1];
        }
        return result;
    }
}


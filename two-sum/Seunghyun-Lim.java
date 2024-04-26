class Solution {
    /**
     * 임의의 두 수를 더해서 target과 동일한 경우
     * 해당하는 두 수의 index를 돌려준다.
     *
     * 두개의 수를 더해서 target과 일치해야 하므로
     * 정답이 항상 2개가 있다고 가정을 하였습니다.
     *
     * 2중 loop를 순회해야 하므로 시간복잡도는 O(n^2)
     * 2개의 값을 저장해야 하므로 공간복잡도는 O(n) 으로 생각됩니다. (틀리다면 리뷰 부탁드립니다 ! )
     * ( => 1개의 값을 저장할때는 공간복잡도가 O(1)이 될까요...? 챗 지피티로 먼저 확인해보겠습니다. )
     *
     * 지피티는 "고정된 저장공간을 사용하기때문에" 공간복잡도는 O(1)이라고 말해주네요!
     * 그렇다면 공간을 가변으로 가지는 ArrayList와 LinkedList의 저장공간은 O(n)이 맞는지도 궁금해지네요
     *
     * @param nums
     * @param target
     * @return
     */
    public static int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    result[0] = i;
                    result[1] = j;

                    return result;
                }
            }
        }

        return result;
    }
}

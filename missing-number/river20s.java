import java.util.Arrays;
class Solution {
    /* [풀이]
     * 1) 배열 nums을 오름차순 정렬한다.
     * 2) 배열 요소의 인덱스와 값을 비교한다.
     *   2-1) 인덱스와 값이 같다면 해당 값은 배열에 있다.
     *   2-2) 인덱스와 값이 다르다면, 해당 값은 배열에 없다.
     * 3) 다른 값의 인덱스를 반환한다.
     * [T.C]
     * 내장된 Arrays.sort()를 사용하면 시간 복잡도는 O(n log n)이 된다.
     * [S.C]
     * 최악의 경우 Arrays.sort()는 추가적으로 O(n) 만큼의 공간을 사용한다.
     */

    public int missingNumber(int[] nums) {
        // nums 오름차순 정렬
        Arrays.sort(nums);
        // 인덱스와 요소 비교
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        // 배열에 없는 값 반환 
        return nums.length
    }
}


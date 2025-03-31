import java.util.Map;
import java.util.HashMap;

class Solution {
    // 정수 배열 nums와 정수 target가 주어질 때 두 정수의 합이 target이 되는 배열 요소의 인덱스를 반환
    // 입력받은 배열에는 하나의 해답만 존재한다고 가정할 수 있으며 같은 요소를 한 번 이상 사용할 수는 없다.
    // 반환하는 인덱스의 정렬은 신경쓰지 않아도 된다.

    public int[] twoSum(int[] nums, int target) {

        // 힌트를 참고하여 시간 복잡도 O(n^2) 이하로 줄이기
        // 힌트: Like maybe a hash map to speed up the search?

        int[] answer = new int[2];

        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (numMap.containsKey(target - nums[i])) {
                answer[0] = numMap.get(target - nums[i]);
                answer[1] = i;
                break;
            }
            numMap.put(nums[i], i);
        }

        return answer;

    }

    // public int[] twoSum(int[] nums, int target) {

    //     // 전체 탐색 진행
    //     int[] answer = new int[2];

    //     for (int i = 0; i < nums.length - 1; i++) {
    //         for (int j = i + 1; j < nums.length; j++) {
    //             if (nums[i] + nums[j] == target) {
    //                 answer[0] = i;
    //                 answer[1] = j;
    //             }
    //         }
    //     }

    //     return answer;
    // }

}

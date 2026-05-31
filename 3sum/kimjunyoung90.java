import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class kimjunyoung90 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answers = new ArrayList<>();
        //숫자들을 미리 정렬해서 3번째 단계에서 추가적인 정렬을 없게 만들자..
        Arrays.sort(nums);

        // 1. 요소가 중복되지 않는 3개의 숫자 조합을 찾음
        for (int i = 0; i < nums.length - 2; i++) {

            //i 값이 전 요소랑 같은 경우 탐색 건너 띄기
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            //two pointer 적용
            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0) {
                    answers.add(Arrays.asList(nums[i], nums[left], nums[right]));

                    //left 중복 체크
                    while (left < right && nums[left] == nums[left + 1]) left++;

                    //right 중복 체크
                    while (left < right && nums[right] == nums[right - 1]) right--;

                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        return answers;
    }
}

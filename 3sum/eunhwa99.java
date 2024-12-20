import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 문제 풀이
 */
// -4 -1 -1 0  2  2
// p1 p2         p3   sum < 0 -> p2 앞으로
// p1    p2      p3   sum < 0 -> p2 앞으로
// p1      p2    p3   sum < 0 -> p2 앞으로
// p1          p2p3   sum = 0 -> p1 앞으로
//    p1 p2      p3   sum = 0 -> p3 값 다른 게 나올 때까지 이동
//    p1 p2 p3        sum < 0 -> p2 앞으로 인데, p2 > p3 되므로 p1 앞으로
//       p1 p2    p3      sum = 0 반복

/**
 * 시간/공간 복잡도
  */
// 시간 복잡도 - 순회 횟수: n + (n-1) + (n-2) + .. => O(N^2)
// 공간 복잡도 - 배열을 정렬하는 데 O(n log n)의 공간 + 결과를 저장하는 answer 리스트는 문제의 요구에 따라 O(k)의 공간 = O(n log n) (배열 정렬을 위한 공간) + O(k) (결과 저장 공간)

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);  // Sort the array first
        List<List<Integer>> answer = new ArrayList<>();

        for (int pointer1 = 0; pointer1 < nums.length - 2; pointer1++) {
            // pointer1 의 중복 값 skip
            if (pointer1 > 0 && nums[pointer1] == nums[pointer1 - 1]) {
                continue;
            }

            int pointer2 = pointer1 + 1;  // pointer2 는 pointer1 의 한 칸 앞
            int pointer3 = nums.length - 1;  // pointer3 는 끝에서 부터

            while (pointer2 < pointer3) {
                int sum = nums[pointer1] + nums[pointer2] + nums[pointer3];

                if (sum < 0) {
                    pointer2++;
                } else if (sum > 0) {
                    pointer3--;
                } else {
                    // sum == 0
                    answer.add(Arrays.asList(nums[pointer1], nums[pointer2], nums[pointer3]));

                    // pointer2 중복 값 제거
                    while (pointer2 < pointer3 && nums[pointer2] == nums[pointer2 + 1]) {
                        pointer2++;
                    }

                    // pointer3 중복 값 제거
                    while (pointer2 < pointer3 && nums[pointer3] == nums[pointer3 - 1]) {
                        pointer3--;
                    }

                    // 두 값 모두 move
                    pointer2++;
                    pointer3--;
                }
            }
        }

        return answer;
    }
}



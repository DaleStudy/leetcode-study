/**
 * 0. 풀이 개요
 *   - 시간복잡도 : O(n^2)
 *   - 공간복잡도 : O(1)
 */

class Solution {
    /**
     * 1. 풀이 과정
     * 1.1 문제 이해
     *   - 세 수의 합이 0이 되는 중복 없는 전체 조합 찾기
     * 1.2 제약 사항
     *   - 인덱스의 조합이 아닌 값의 조합이므로 배열의 원본을 유지할 필요는 없음
     *   - 조합의 중복을 어떻게 제외 시킬지가 관건
     * 1.3 풀이 아이디어
     *   - 하나의 값이 고정되어 있으면 나머지 두 원소의 합이 고정값 * -1 이 되어야 하는 형태라고도 볼 수 있음
     *   - 배열의 인덱스는 몰라도 되므로 배열을 오름차순으로 정렬할 수 있음
     *   - 이때 고정값 하나는 반복문 안에서 루프를 돌면서 정하고, 나머지 두 수는 투 포인터로 원하는 조합을 찾을 수 있음
     *   - 배열이 오름차순으로 정렬되어 있으므로, 만약 합이 0 보다 크다면 숫자가 작아져야 하고, 0보다 작다면 숫자가 커져야 함. 
     *   - 따라서 세 수의 합이 작아져야 한다면 우측 포인터를 좌측으로 옮기면서 숫자를 줄일 수 있고,
     *   - 합이 커져야 한다면 좌측 포인터를 우측으로 옮기면서 전체 합을 키울 수 있음.
     *   - 여기에 더해 중복을 제외하기 위해서 같은 수의 경우는 포인터를 건너뛰는 식으로 처리할 수 있음.
     *   - 시간복잡도는 배열의 원소(n)만큼 루프를 돌면서, 그 안에서 최악의 경우 n - 2 번 순회 하게 되므로 N(N-2) 가 되어 n^2 이라 볼 수 있음.
     *   - 추가적인 공간을 일부 만들기는 하는데 n에 차수에 대응하는 수가 없으므로 공간복잡도는 O(1)로 판단.
     */
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();

        for(int i=0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i+1;
            int right = nums.length - 1;

            while(left < right) {
                if(nums[i] + nums[left] + nums[right] == 0) {
                    List<Integer> triple = List.of(nums[i], nums[left], nums[right]);
                    answer.add(triple);
                    while(left+1 < right && nums[left] == nums[left+1]) left++;
                    while(right > 0 && nums[right] == nums[right-1]) right--;
                    left++;
                    right--;
                } else if(nums[i] + nums[left] + nums[right] > 0) right--;
                else left++;
            }
        }

        return answer;
    }
}

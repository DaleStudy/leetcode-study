import java.util.*;

/**
    풀이 :
        정렬을 한 뒤, 한점을 기준점으로 삼고, 투 포인터를 이용하여 결과 배열을 구하는 방식

    복잡도 계산 :
        매개변수 nums의 길이 -> N
        시간 복잡도 : O(N^2)
        공간 복잡도 : O(N^2)
*/
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i < nums.length-2; i++) {

            // 이전과 같은 기준점이 나오면, 중복으로 result에 등록될 수 있으므로, continue
            if(i > 0 && nums[i] == nums[i - 1]){
				continue;
			}

            // 정렬한 상황에서 기준점이 양수가 나오면, 사실상 불가능
            if(nums[i] > 0){
                break;
            }

            int targetSum = 0 - nums[i];

            int left = i + 1;
            int right = nums.length - 1;
            

            while(left < right) {
                if((nums[left] + nums[right]) > targetSum) {
                    right--;
                }else if((nums[left] + nums[right]) < targetSum) {
                    left++;
                }else {
                    // 중복 데이터 추가에 대한 if문
                    if((right == nums.length - 1) || (nums[right] != nums[right+1])) {
                        result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    }
                    left++;
                    right--;
                }
            } 
        }
        return result;
    }
}

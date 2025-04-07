import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// 시간 복잡도: O(n^2) - nums 배열을 정렬하는 데 O(nlogn) 소요, 이후 이중 포인터로 O(n^2)
// 공간 복잡도: O(1) - 결과 리스트를 제외한 추가 공간 사용 없음
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        Arrays.sort(nums);

        List<List<Integer>> result = new ArrayList<>();

        for(int i=0;i<nums.length-2;i++){
            if(i>0 && nums[i] == nums[i-1]) continue; // 중복된 값 건너뛰기
            int left = i+1;
            int right = nums.length-1;

            while(left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if(sum == 0){
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    while(left < right && nums[left] == nums[left+1]) left++; // 중복된 값 건너뛰기
                    while(left < right && nums[right] == nums[right-1]) right--; // 중복된 값 건너뛰기
                    left++;
                    right--;
                } else if(sum < 0){
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
    }
}

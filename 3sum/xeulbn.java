import java.util.*;

//시간복잡도 : O(n^2), 공간복잡도 : O(nlogn)

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();

        for(int i=0;i<nums.length-2;i++){
            if (i>0 && nums[i] == nums[i-1]) {
                continue;
            }
            int leftIndex = i+1;
            int rightIndex = nums.length-1;

            while(leftIndex<rightIndex){
                int sum =nums[i]+nums[leftIndex]+nums[rightIndex];

                if(sum==0){
                    // 정답 추가
                    List<Integer> tmpList = new ArrayList<>();
                    tmpList.add(nums[i]);
                    tmpList.add(nums[leftIndex]);
                    tmpList.add(nums[rightIndex]);

                    answer.add(tmpList);

                    // left++, right--
                    leftIndex+=1;
                    rightIndex-=1;

                    // 중복 제거
                    while(leftIndex<rightIndex && nums[leftIndex]==nums[leftIndex-1]){
                        leftIndex+=1;
                    }
                    while(leftIndex<rightIndex && nums[rightIndex]==nums[rightIndex+1]){
                        rightIndex-=1;
                    }

                }else if(sum<0){
                    leftIndex+=1;
                }else{
                    rightIndex-=1;
                }
            }
        }

        return answer;
    }
}

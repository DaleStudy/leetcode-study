/**
    풀이 :
        for문을 통해 맨 앞, 맨 뒤부터 순회하면서 곱연산을 함.

    복잡도 계산 :
        매개변수 nums의 길이 -> N
        시간 복잡도 : O(N)
        공간 복잡도 : O(N)
*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] resultList=new int[nums.length];
        Arrays.fill(resultList,1);
        int result = 1;
        for(int i=0; i<nums.length-1;i++){
            result*=nums[i];
            resultList[i+1]*=result;
        }
        result = 1;
        for(int i=nums.length-1; i>0;i--){
            result*=nums[i];
            resultList[i-1]*=result;
        }
        return resultList;
    }
}

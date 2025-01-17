// 단순하게 정렬해서 일치하지 않으면 출력하고 리스트를 벗어나면 그대로 checkNum을 출력하는 방식
// 시간복잡도 : O(NlogN)
// 공간복잡도 : O(1)

class SolutionGotprgmer {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int checkNum = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i] != checkNum){
                return checkNum;
            }
            checkNum += 1;
        }
        return checkNum;

    }
}

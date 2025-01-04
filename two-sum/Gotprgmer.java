// 배열을 정렬하여 투포인터로 접근하여 풀었습니다.
// 정렬된 배열의 인덱스를 찾기 위해 indexOf 메소드를 만들어서 사용했습니다.

// 시간복잡도 : O(NlogN) -> 정렬을 위해 O(NlogN) + 투포인터로 O(N)이므로 O(NlogN)
// 공간복잡도 : O(N) -> 정렬을 위해 복사한 배열이 필요하므로 O(N)
class SolutionGotprgmer {
    public int[] twoSum(int[] nums, int target) {
        int[] original = new int[nums.length];

        for(int i=0;i<nums.length;i++){
            original[i] = nums[i];
        }
        Arrays.sort(nums);

        int l = 0;
        int r = nums.length-1;
        while (l<r){
            int lV = nums[l];
            int rV = nums[r];
            int total = lV + rV;
            if(total > target){
                r -= 1;
            }
            else if(total < target){
                l += 1;
            }
            else{
                int[] ans = indexOf(lV,rV,original);
                l = ans[0];
                r = ans[1];
                break;
            }
        }
        return new int[] {l,r};
    }

    public int[] indexOf(int l,int r, int[] nums){
        int lIdx = -1;
        int rIdx = -1;
        for(int i = 0;i<nums.length;i++){
            if(nums[i] == l){
                lIdx = i;
                break;
            }
        }
        for(int i = nums.length-1;i>-1;i--){
            if(nums[i] == r){
                rIdx = i;
                break;
            }
        }
        return new int[] {lIdx,rIdx};
    }
}

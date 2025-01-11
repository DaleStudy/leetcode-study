class Solution {

    // lenArr[i] : i를 마지막 원소로 하는 최장 부분 수열 길이
    // 시간 복잡도: O(N*N) -> 이중 반복문
    // 공간 복잡도: O(N) -> 배열 크기
    public int lengthOfLIS(int[] nums) {
        int[] lenArr = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            lenArr[i] = 1; 
            for(int j=0;j<i;j++){
               if(nums[i]>nums[j]){
                lenArr[i] = Math.max(lenArr[j] +1, lenArr[i]); 
                // j번째 숫자를 수열에 포함시키거나 포함시키지 않음 -> 두 개 비교해서 Max 값 찾는다.
               }
            }
        }

        int result = 0;
        for(int i=0;i<nums.length;++i){
            result = Math.max(lenArr[i], result);
        }

        return result;
    }
}

// 2번째 풀이 -> BinarySearch 로도 가능하다...!
// 시간 복잡도 : O(NlogN)
// 공간 복잡도: O(N)
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] list = new int[nums.length];
        int j = -1;
        for(int i=0;i<nums.length;i++){
            if (j == -1 || list[j] < nums[i]) {
                list[++j] = nums[i];
            } 
            else{
                int left = 0, right = j;
                while(left<right){
                    int mid = left + (right - left) / 2;

                    if(list[mid]<nums[i]) left = mid + 1; 
                    // nums[i]는 list[mid]보다 크므로 nums[i]는 mid 오른쪽에 위치해야 함 -> 따라서 left = mid + 1로 범위를 좁힌다.
                    else right = mid;
                }
                list[left] = nums[i];

            }
        }
         
        return j + 1;
    }

}

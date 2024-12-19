// 해당 문제는 dfs로 풀이 하던 도중, 시간제한으로 풀지 못하였습니다.
// 이후 답을 참고하였고, 메모이제이션을 떠올리게 되었습니다.
// 풀이 아이디어는 i번째 인덱스를 선택한 합과 i+1번째 인덱스를 선택한 합중에 큰 것을 선택하는 것이 가장 큰 아이디어 였습니다.
// 그런데 중복된 과정이 존재하기에 메모이제이션을 활용하여
// 원래는 O(2^N)의 시간복잡도를
// 각 인덱스에 해당하는 함수호출을 1번씩만 하도록 유도하여 시간복잡도를 해결하였습니다.
// 시간복잡도 : O(N)
// 공간복잡도 : O(N)

class SolutionGotprgmer {
    static int[] memo;
    static int answer;
    public int rob(int[] nums) {
        answer = 0;
        memo = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            memo[i] = -1;
        }
        return dfs(nums,0);
    }
    public int dfs(int[] nums, int idx){
        if(idx<nums.length){

            if(memo[idx] != -1){
                return memo[idx];
            }
            else{
                memo[idx] = Math.max(nums[idx]+dfs(nums,idx+2),dfs(nums,idx+1));
                return memo[idx];
            }
        }
        else{
            return 0;
        }


    }
}

/** 시간초과 발생합니다. 해법 찾는 중입니다 */
class Solution {
    public int longestConsecutive(int[] nums) {
        
        Set<Integer> uniqueNum = new HashSet<>();
        for (int num : nums) { // 수열 내 중복 숫자 제거
            uniqueNum.add(num);
        }

        int uniqueLen = uniqueNum.size();
        int longest = 0;

        for(int targetNum: uniqueNum){

            int n = 1;
            for(int j = targetNum + 1; j < targetNum + uniqueLen; j++) {
                if (!uniqueNum.contains(j)) break;
                n++;
            }
            longest = Math.max(n, longest);

        }
        return longest;
    }
}

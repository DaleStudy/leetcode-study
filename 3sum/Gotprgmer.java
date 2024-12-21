// 이전에 투포인터를 활용하여 시도했지만 중복된 값들을 처리하는데 어려움이 있었습니다.
// 그래서 해답을 보았고 새로운 방법으로 풀어보았습니다.
// 서로 다른 i와 j 인덱스를 2중 for문으로 진행하면서
// i와 j사이 수들을 set으로 관리합니다.
// set에 -nums[i]-nums[j]가 존재하면 결과 리스트에 추가합니다.
// 시간복잡도 : O(N^2)
// 공간복잡도 : O(N)
class SolutionGotprgmer {
    public List<List<Integer>> threeSum(int[] nums) {
        // 결과를 저장할 리스트
        List<List<Integer>> result = new ArrayList<>();
        Set<Integer> set;
        Set<List<Integer>> resultSet = new HashSet<>();
        List<Integer> numList;


        // 리스트 정렬
        Arrays.sort(nums);
        for(int i=0;i<nums.length-2;i++){
            if (i > 0 && nums[i - 1] == nums[i]) continue;

            set = new HashSet<>();
            for(int j=i+1;j<nums.length;j++){
                int checkNum = nums[i]+nums[j];
                if(set.contains(-checkNum)){
                    numList = new ArrayList<>(Arrays.asList(nums[i], -checkNum, nums[j]));
                    if(!resultSet.contains(numList)){
                        result.add(numList);
                        resultSet.add(numList);
                    }
                }
                set.add(nums[j]);
            }
        }
        return result;
    }
}

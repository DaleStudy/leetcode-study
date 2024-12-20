// 투포인터 방식으로 구현 
// 투포인터의 기본 시간복잡도가 O(2^n)이므로 오름차순으로 정렬하는 O(NlogN)은 마음껏 사용해도 된다.
public List<List<Integer>> threeSum(int[] nums) {
    List<List<Integer>> result = new ArrayList<>();
    Arrays.sort(nums);
    for(int i =0; i< nums.length-2;i++) {
        if (i > 0 && nums[i] == nums[i - 1]) continue;
        int left = i + 1, right = nums.length - 1;
        while (left < right) {
            int sum = nums[i] + nums[left] + nums[right];

            if (sum == 0) {
                result.add(Arrays.asList(nums[i], nums[left], nums[right]));

                while (left < right && nums[left] == nums[left + 1]) left++;
                while (left < right && nums[right] == nums[right - 1]) right--;

                left++;
                right--;
            } else if (sum < 0) {
                left++;
            } else {
                right--;
            }
        }
    }
    return result;
}


// dfs 풀이를 생각했으나 dfs 방식은 무조건 O(2^n)의 결과가 나온다.
// 타임 아웃 오답
public class Solution {
   public List<List<Integer>> threeSum(int[] nums) {
       Set<List<Integer>> answerSet = new HashSet<>();
       nums = Arrays.stream(nums).sorted().toArray();  
       dfs(nums, 0, new ArrayList<>(), answerSet);
       return new ArrayList<>(answerSet);
   }

   public void dfs(int[] nums, int index, List<Integer> temp, Set<List<Integer>> answerSet) {
       if (temp.size() == 3) {
           int result = 0;
           for (int element : temp) result += element;
           if (result == 0) answerSet.add(new ArrayList<>(temp));
           return;
       }

       for (int i = index; i < nums.length; i++) {
           temp.add(nums[i]);
           dfs(nums, i + 1, temp, answerSet);
           temp.remove(temp.size() - 1);
       }
   }
}

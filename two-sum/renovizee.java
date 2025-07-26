import java.util.HashMap;
import java.util.Map;

// tag renovizee 1week
// https://github.com/DaleStudy/leetcode-study/issues/219
// https://leetcode.com/problems/two-sum/description/

// #요구사항 요약
// 1. int[] nums와 int target이 주어진다.
// 2. nums의 두 수의 합이 target과 같은 int[] index를 리턴한다. (순서 상관 x)
// 3. 똑같은 원소를 두번 사용하지 못하고, 정확히 하나의 정답만 있다.

class Solution {
    // Solv3: map 최적화
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for (int i = 0; i < nums.length; i++) {
            int key = target - nums[i];
            if (map.containsKey(key) && map.get(key) != i) {
                result[0] = i;
                result[1] = map.get(key);
            }
            map.put(nums[i], i);
        }
        return result;
    }
//-------------------------------------------------------------------------------------------------------------
    // Solv2: map
    // 시간복잡도 : O(n)
    // 공간복잡도 : O(n)
//    public int[] twoSum(int[] nums, int target) {
//        Map<Integer, Integer> map = new HashMap<>();
//        int[] result = new int[2];
//        for (int i = 0; i < nums.length; i++) {
//            map.put(nums[i], i);
//        }
//
//        for (int i = 0; i < nums.length; i++) {
//            int key = target - nums[i];
//            if (map.containsKey(key) && map.get(key) != i) {
//                result[0] = i;
//                result[1] = map.get(key);
//            }
//        }
//        return result;
//
//    }
//-------------------------------------------------------------------------------------------------------------
//    Solv1: Brute Force
//    시간복잡도 : O(n^2)
//    공간복잡도 : O(1)
//    public int[] twoSum(int[] nums, int target) {
//        int size = nums.length;
//        for(int i = 0; i < size - 1; i++) {
//            for(int j = i+1; j < size; j++) {
//                if(target == (nums[i] + nums[j])){
//                    return new int[]{i,j};
//                }
//            }
//        }
//        return new int[]{};
//    }


// 1) ==: 두 값이 같은지 비교. 기본 타입은 값을 비교하고, 참조 타입은 메모리 주소(동일한 객체인지)를 비교
// 참조 타입 객체의 내용이 같은지를 비교하려면 주로 a.equals(b)를 사용
//
// 2) 초기화 배열과 맵
// - new int[2] :size 초기화
// - new int[]{1,2,3} : 실제 값 초기화
// - Map<String,String> test = new HashMap<>(); 맵의 k/v 타입은 앞 변수에 설정한다. val 만사용하다..
//-------------------------------------------------------------------------------------------------------------

}

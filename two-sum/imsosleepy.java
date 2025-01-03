// hashmap 조회 방식은 O(N)
// 3ms
public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    return null;
}

// 첫 생각 : 정렬 -> 투포인터
public int[] twoSum1(int[] nums, int target) {
    Arrays.sort(nums);
    int left = 0;
    int right = nums.length-1;
    int sum = 0;
    while(left < right) {
        sum = nums[left] + nums[right];
        if(target > sum) {
            left++;
        }
        if(target < sum) {
            right--;
        }
        if(target == sum) {
            break;
        }
    }
    return new int[]{left, right};
}

// 투포인터는 O(N)에 충족하지만 정렬이 nlog(n)임
// 9ms
public int[] twoSum2(int[] nums, int target) {
    int[][] indexedNums = new int[nums.length][2];
    for (int i = 0; i < nums.length; i++) {
        indexedNums[i][0] = nums[i]; 
        indexedNums[i][1] = i;      
    }

    Arrays.sort(indexedNums, Comparator.comparingInt(a -> a[0]));

    int left = 0, right = nums.length - 1;
    while (left < right) {
        int sum = indexedNums[left][0] + indexedNums[right][0];
        if (sum == target) {
            return new int[] { indexedNums[left][1], indexedNums[right][1] }; 
        } else if (sum < target) {
            left++;
        } else {
            right--;
        }
    }
    return new int[]{left, right};
}

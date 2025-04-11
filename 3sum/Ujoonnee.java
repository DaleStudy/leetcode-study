import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], i);
        }

        Set<Triplet> set = new HashSet<>();
        for(int i = 0; i < nums.length; i++) {
            int target = -nums[i];
            for(int j = i+1; j < nums.length; j++) {
                int operand = target - nums[j];
                if (map.containsKey(operand) && map.get(operand) > j) {
                    set.add(new Triplet(nums[i], nums[j], operand));
                }
            }
        }

        return set.stream().map(t -> List.of(t.triplet[0], t.triplet[1], t.triplet[2])).collect(Collectors.toList());
    }
}

class Triplet {
    int[] triplet;

    Triplet(int first, int second, int third) {
        this.triplet = new int[] { first, second, third };
        Arrays.sort(triplet);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Triplet that)) {
            return false;
        }

        for(int i = 0; i<3; i++) {
            if (this.triplet[i] != that.triplet[i]) {
                return false;
            }
        }

        return true;
    }

    @Override
    public int hashCode() {
        return Objects.hash(triplet[0], triplet[1], triplet[2]);
    }
}
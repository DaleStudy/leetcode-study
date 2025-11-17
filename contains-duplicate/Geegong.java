import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

public class Geegong {


    /**
     * time complexity : O(n)
     * space complexity : o(n)
     * @param nums
     * @return boolean
     */
    public boolean containsDuplicate(int[] nums) {



        HashSet<Integer> uniques = new HashSet<>();

        for (int num : nums) {

            // 명확하게 hashSet에 값이 있는지 체크하는 메소드로 확인이 가능하지만
//            if (uniques.contains(num)) {
//                return true;
//            }
//            uniques.add(num);

            // hashSet 의 Add 는 이미 값이 있다면 FALSE를 리턴하기에 아래처럼도 동작 가능 (더 빠른 결과확인)
            if (!uniques.add(num)) {
                return true;
            }
        }

        return false;
    }

}


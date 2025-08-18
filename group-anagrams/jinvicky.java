import java.util.*;
import java.util.stream.Collectors;

class Solution {
    /**
     * 41ms를 가진 낮은 성능의 첫번째 정답 코드
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        // 길이가 1이면 자체를 List로 감싸서 반환한다. 
        if (strs.length == 1) {
            return List.of(List.of(strs[0]));
        }

        List<List<String>> groupList = new ArrayList<>();
        /**
         * bf로 그룹핑을 할 수 있나?
         * strs를 for문으로 돌면서 "정렬한" 단어가 map에 있는 지 확인하고 존재할 경우 key로 조회한 list에 추가한다.
         * 마지막으로 map을 순회하면서 list들을 groupList.add(list); 한다. 
         */
        Map<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            String sortedS = Arrays.stream(s.split(""))
                    .sorted()
                    .collect(Collectors.joining());
            List<String> v = map.get(sortedS);
            if (v == null) {
                map.put(sortedS, new ArrayList<>());
            }
            map.get(sortedS).add(s);
        }

        for (List<String> list : map.values()) {
            groupList.add(list);
        }
        return groupList;
    }
}
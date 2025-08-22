import java.util.*;

public class Geegong {

    /**
     * case 1. HashMap<String, List<String>> 으로 velues 를 리턴하는 방법
     * key 값은 strs 의 각 str 들을 char array 로 변환한 후 sorting 한다.
     * 그럼 동일한 letter 들을 갖는 아이들은 소팅 후에 동일한 char array 를 가지므로 그룹핑이 가능함
     *
     * TimeComplexity:
     *  O(N * L log L) = O(N)
     * -> N 은 strs 의 갯수
     * -> L 은 str 의 길이
     * -> L long L 은 str의 sorting 시간 복잡도
     *
     * space complexity: O(N)
     *
     * case 2. key : lower letter 들만 보장이 된 경우 char[26] 인 배열들에 대해서 인덱스가 0 ~ 25 까지 'a' ~ 'z' 위 값을 의미한다고 하면
     * letter 별로 카운트를 해당되는 인덱스에 +1 씩 하고 구분자('#")로 각 letter 별 횟수를 구분할 수 있는 key 를 만들어
     * 결국 case1과 유사하게 str 에 해당되는 key 를 갖는 List<String> 을 갖는 hashMap 을 가지게 하는 방법
     *
     * Time complexity :
     * O(L * N) = O(N)
     *
     * Space complexity :
     * O(N)
     *
     * @param strs
     * @return
     */
    public List<List<String>> groupAnagrams(String[] strs) {
        // case 1.
//        Map<String, List<String>> resultMap = new HashMap<>();
//
//        for (String str : strs) {
//            char[] chars = str.toCharArray();
//            // sort
//            Arrays.sort(chars);
//            String key = new String(chars);
//            // key : sorted str, value : strs
//            resultMap.computeIfAbsent(key, k -> new ArrayList<>()).add(str);
//        }
//
//        return new ArrayList<>(resultMap.values());

        // case 2.
        Map<String, List<String>> resultMap = new HashMap<>();
        for (String str : strs) {
            char[] chars = str.toCharArray();
            char[] numberOfLetters = new char[26]; // 'a' ~ 'z'
//            Arrays.copyOf()

            for (char eachChar : chars) {
                numberOfLetters[eachChar - 'a']++; // 각 character 에 해당되는 배열의 인덱스에 1씩 값을 더해간다 ex) aba => ['2', '0', '0', ... ,'0'] / abfcb = ['1', '2', '1', '0', '0', '1', '0'...'0']
            }

            StringBuilder keyMaker = new StringBuilder(2 * 26);
            for (char numberOfLetter : numberOfLetters) {
                keyMaker.append(numberOfLetter).append("#");
            }

            resultMap.computeIfAbsent(keyMaker.toString(), input -> new ArrayList<>()).add(str);
        }

        return new ArrayList<>(resultMap.values());
    }


}

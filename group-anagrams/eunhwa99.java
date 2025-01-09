import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// 해결법
// 1. 배열 안의 월소들을 순회한다.
// 2. 각 원소에 대하여 문자열을 정렬한 후, hashmap에 넣는다. 이 때 hashMap 자료구조는 <String, List<String>> 형태로 만든다.

// 시간 복잡도: 
// 1. 크기가 m인 문자열을 정렬할 때 O(mlogm)이 소요
// 2. 배열의 크기가 n 이므로 순회하는데 O(n)
// 3. hashmap 삽입은 O(1)
// 위 사실들을 조합하면 총 O(nmlogm)이 소요된다.
// 참고로, 전체 배열 크기는 최대 10^4 이고, 각 문자열의 길이는 최대 100이므로, 위와 같이 접근할 경우, 최대 10^6의 시간 복잡도를 가진다.

// 공간 복잡도: hashmap 크기만큼 사용 -> O(nm)

class Solution{
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(String str: strs){
            char[] charArr = str.toCharArray();
            Arrays.sort(charArr);

            map.computeIfAbsent(String.valueOf(charArr), key -> new ArrayList<>()).add(str);
        }
        return map.values().stream().toList();
    }
}

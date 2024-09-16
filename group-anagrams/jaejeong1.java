import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class SolutionGroupAnagram {
  public List<List<String>> groupAnagrams(String[] strs) {
    // char, integer map으로 strs의 원소들을 분류한다
    // 분류 후 알파벳 순으로 정렬해 알파벳 + 개수 조합의 str으로 만든다
    // str 과 인덱스를 맵에 넣는다
    // 맵 keyset을 돌면서 value에 해당하는 strs 인덱스로 접근해 정답으로 반환
    // 시간복잡도: O(N^2), 공간복잡도: O(N)
    Map<String, List<Integer>> map = new HashMap<>();

    for (int i=0; i<strs.length; i++) {
      var anagramData = createAnagramData(strs[i]);
      var value = map.getOrDefault(anagramData, new ArrayList<>());
      value.add(i);
      map.put(anagramData, value);
    }

    List<List<String>> answer = new ArrayList<>();

    for (String key : map.keySet()) {
      List<String> value = new ArrayList<>();
      for (int index : map.get(key)) {
        value.add(strs[index]);
      }

      answer.add(value);
    }

    return answer;
  }

  private String createAnagramData(String str) {
    Map<Character, Integer> map = new HashMap<>();

    for (int i=0; i<str.length(); i++) {
      var element = str.charAt(i);
      map.put(element, map.getOrDefault(element, 0)+1);
    }

    var keySet = map.keySet().stream().sorted().toList();
    StringBuilder anagramData = new StringBuilder();
    for (char key : keySet) {
      anagramData.append(key).append(map.get(key));
    }

    return anagramData.toString();
  }
}

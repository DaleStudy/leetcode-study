import java.util.HashMap;
import java.util.Map;

class SolutionValidAnagram {
  public boolean isAnagram(String s, String t) {
    // 풀이: 해시맵을 사용해 s와 t의 문자 별 빈도수를 저장한다
    // 두 빈도수의 모든 키와 값이 같고, 크기가 같은지 비교한다.
    // 다르다면 false를 반환, 모두 같다면 true를 반환한다.
    // 시간복잡도: O(N), 공간복잡도: O(1)

    Map<Character, Integer> sAnagram = createAnagramMap(s);
    Map<Character, Integer> tAnagram = createAnagramMap(t);

    // 두 해시맵의 크기가 같은지 확인
    if (sAnagram.size() != tAnagram.size()) {
      return false;
    }

    // sAnagram과 tAnagram의 모든 키와 값을 비교
    for (Map.Entry<Character, Integer> entry : sAnagram.entrySet()) {
      var key = entry.getKey();
      int value = entry.getValue();

      // tAnagram에 key가 존재하지 않거나, 그에 대응하는 value가 다르면 false 반환
      if (!tAnagram.containsKey(key) || !tAnagram.get(key).equals(value)) {
        return false;
      }
    }

    return true;
  }

  private Map<Character, Integer> createAnagramMap(String text) {
    Map<Character, Integer> anaGramMap = new HashMap<>();

    for (var c: text.toCharArray()) {
      anaGramMap.put(c, anaGramMap.getOrDefault(c, 0) + 1);
    }

    return anaGramMap;
  }
}

import java.util.HashMap;
import java.util.Map;

// insert 시, 문자열의 prefix를 다 Map에 저장하고, 해당 문자열은 prefix 이므로 boolean false 로 설정
// prefix가 아닌 온전한 문자열 삽입은 true 로 저장

// search 시, Map에 해당 단어가 있는지 확인하고, boolean 값이 true 인지 확인
// startsWith는 그냥 Map 에 해당 문자열이 있는지 확인하면 된다.

// 공간 복잡도: Map 크기 -> O(N)
// 시간 복잡도: 전체 호출 수 * String 길이 -> O(N*M)
// 참고) 최대 시간 복잡도 : 2000 * 3*10^4 = 6*10^7
class Trie {

    Map<String,Boolean> stringSet;
    public Trie() {
        stringSet = new HashMap<>();
    }
    
    public void insert(String word) {
        for(int i=0;i<word.length();i++){
            stringSet.putIfAbsent(word.substring(0, i), false);
        }
      stringSet.put(word, true);
    }
    
    public boolean search(String word) {
        return stringSet.containsKey(word) && stringSet.get(word)==true;
    }
    
    public boolean startsWith(String prefix) {
       
        return stringSet.containsKey(prefix);
    }
}

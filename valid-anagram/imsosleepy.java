// 자바에서는 시간복잡도를 O(N)으로 잡아도 최상위권으로 갈 수 없는 문제
// 유니코드 고려
public boolean isAnagram(String s, String t) {
    if (s.length() != t.length()) return false;

    Map<Character, Integer> map = new HashMap<>();
    for (int i = 0; i < s.length(); i++) {
        map.put(s.charAt(i), map.getOrDefault(s.charAt(i), 0) + 1);
        map.put(t.charAt(i), map.getOrDefault(t.charAt(i), 0) - 1);
    }
    for (int value : map.values()) {
        if (value != 0) return false;
    }
    return true;
}
// 알파벳만 고려
public boolean isAnagram(String s, String t) {
    int ALPHABET_COUNT = 26;
    if(s.length() != t.length()) {
        return false;
    }
    int[] arr = new int[ALPHABET_COUNT]; // 알파벳 갯수
    for(int i = 0; i < s.length() ; i ++) {
        arr[s.charAt(i) - 97]++;
        arr[t.charAt(i) - 97]--;
    }
    for(int i = 0; i < ALPHABET_COUNT; i ++) {
        if(arr[i] != 0) {
            return false;
        }
    }
    return true;
}

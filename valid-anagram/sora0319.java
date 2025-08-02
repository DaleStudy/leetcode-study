// Map을 사용한 버전
class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        Map <Character, Integer> alphabet = new HashMap<>();

        for(char c : s.toCharArray()){
            if(!alphabet.containsKey(c)){
                alphabet.put(c, 0);
            }
            alphabet.put(c, alphabet.get(c) + 1);
        }

        for(char c : t.toCharArray()){
            if(!alphabet.containsKey(c)) return false;
            if(alphabet.get(c) == 0) return false;

            alphabet.put(c, alphabet.get(c)-1);
        }

        return true;
    }
}


// 초기 버전
class Solution {
    public boolean isAnagram(String s, String t) {
        int[] character = new int[26];
        if(s.length() != t.length()) return false;

        for(int i = 0; i < t.length(); i++){
            int place = t.charAt(i) - 'a';
            character[place]++;
        }

        for(int i = 0; i < s.length(); i++){
            int place = s.charAt(i) - 'a';
            if(character[place] <= 0) return false;
            character[place]--;
        }
        return true;
    }
}

/*
Map, 배열 모두 평균시간복잡도는 O(1)이지만, 
배열이 직접 접근 방식이고, Map은 Hash를 사용하여서 배열 보다는 시간이 더 걸린다
배열 사용시 4ms
Map 사용 시 17ms 
*/

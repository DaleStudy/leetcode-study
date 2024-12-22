// 각 s와 t의 알파벳 수를 카운팅 시켜서 마지막에 카운팅이 모두 같으면 true
// 그렇지 않으면 false;

// 시간복잡도 O(N) => 1중 for문
// 공간복잡도 O(N) => N개 알파벳이 들어있는 Map 2개
class SolutionGotprgmer {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> sMap = new HashMap<>();
        Map<Character,Integer> tMap = new HashMap<>();
        if(s.length() != t.length()){
            return false;
        }
        for(int i=0;i<s.length();i++){
            char sChar = s.charAt(i);
            char tChar = t.charAt(i);
            sMap.put(sChar,sMap.getOrDefault(sChar,0)+1);
            tMap.put(tChar,tMap.getOrDefault(tChar,0)+1);
        }
        boolean flag = true;
        for(char c:sMap.keySet()){
            if(!sMap.getOrDefault(c,0).equals(tMap.getOrDefault(c,0))){
                flag = false;
                System.out.println(c);
                break;
            }
        }

        return flag;
    }
}

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

// DFS 완전탐색할 때 불필요한 탐색을 줄이는 방법을 항상 고민할 것.
class Solution {
    public int size = 0;
    public Map<String, Boolean> failedMap = new HashMap<>();
    public boolean wordBreak(String s, List<String> wordDict) {
        size = wordDict.size();

        Set<Character> sSet = new HashSet<>();
        for (char c : s.toCharArray()) {
            sSet.add(c);
        }   

        Set<Character> wSet = new HashSet<>();
        for (char c : String.join("", wordDict).toCharArray()) {
            wSet.add(c);
        }

        if(sSet.size() > wSet.size()) {
            return false;
        }

        return dfs(s, wordDict);
    }

    public boolean dfs(String s, List<String> wordDict) {
        if(s.length() == 0) return true;
        if(failedMap.containsKey(s)) return false;

        for(int i = 0; i < size; i++) {
            String word = wordDict.get(i);
            if(s.startsWith(word)) {

                s = s.substring(word.length());
                boolean result = dfs(s, wordDict);

                if(result) {
                    return true;
                } else {
                    failedMap.put(s, true);
                }

                s = word + s;                
            }
        }

        return false;
    }
}

// 특정 문자로 시작되는 것만 판단하여 반복해 풀려고 했던 접근법.
// 전체 조합을 보아야 하는 "cars", ["cars", "ca", "rs"] 경우에 반례가 됨.
class WrongSolution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int size = wordDict.size();
        
        while(true) {
            boolean isMatched = false;
            for(int i = 0; i < size; i++) {
                String word = wordDict.get(i);
                if(s.startsWith(word)) {
                    isMatched = true;
                    s = s.substring(word.length());
                    break;
                }
            }

            if(!isMatched) {
                break;
            }
        }

        return s.length() == 0;   
    }
}

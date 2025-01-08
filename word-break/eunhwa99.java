import java.util.List;


// 풀이
// dfs + memo 
// memo[i] = true/false : i 인덱스에서 시작해서 wordDict에 존재하는 모든 부분문자열 찾을 수 있는 경로가 있는지 유무
//시간 복잡도: O(n*n) = start~end(재귀) + start~end(반복문)
// 공간 복잡도: O(n) - 재귀 깊이

class Solution {
    
    public boolean wordBreak(String s, List<String> wordDict) {
        return dfs(0, s.length(), s, wordDict, new Boolean[s.length()]);

    }
    public boolean dfs(int start,  int len, String s, List<String> wordDict, Boolean[] memo){
        if(start==len){
            return true;
        }

        if(memo[start]!=null) return memo[start]; 

        for(int end=start+1; end<=len;end++){
            if(wordDict.contains(s.substring(start, end))){
                if(dfs(end, len, s, wordDict, memo)){
                    memo[start] = true; 
                    return true;
                }
            }
        }

       memo[start]=false;
       return false;

    }
}

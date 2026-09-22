/**
 * n: 문자열 s의 길이, m: wordDict 단어 수, k: 단어의 평균 길이
 * - TC: O(n * m * k) -> n개 인덱스 방문 × m개 단어 순회 × k 길이 문자열 비교
 * - SC: O(n)          -> 메모이제이션 배열 및 재귀 스택 깊이 O(n)
 */
class Solution {
    String s;
    int len = 0;
    boolean[] imposible;
    List<String> wordDict;
    
    public boolean wordBreak(String s, List<String> wordDict) {
        this.s = s;
        this.len = s.length();
        this.imposible = new boolean[len];
        this.wordDict = wordDict;
        return dfs(0);
    }

    public boolean dfs(int index) {
        if(index == len) {
            return true;
        }

        if(imposible[index]) return false; 

        for(String word : wordDict) {
            int wordLength = word.length();
            if(s.startsWith(word, index)) {
                if(len >= index + wordLength) {
                   if(dfs(index + wordLength)) return true; 
                }
            }
        }

        imposible[index] = true;
        return false;
    }
}

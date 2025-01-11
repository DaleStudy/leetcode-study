/**
 input : string s and array of strings
 output : return true if s can be segmented into one or more words in dictionary
 constraints :
 1) same word can be used multiple times
 2) every word in dictionary is unique
 3) s.length [1, 300]
 4) length of tokens in dictionary [1, 20]

 ex)
 leetcode >> leet code
 applepenapple >> apple pen
 applepenapple >> apple applepen


 solution 1) bruteforce
 for each character c, check if word exists in dictionary
 that the first letter is c

 match string
 move to next
 unmatch
 next word

 >> get all the combinations
 O(n * m * k)
 n is the length of string s,
 m is number of tokens,
 k is length of token

 tc : O (nmk) (300 * 1000 * 20) ~= 6 * 10^6 < 1sec
 sc : O (mk)

 solution 2) optimize? heuristic?

 using trie will reduce tc
 for each character:
 get all substring substr(i, j)
 search trie

 tc : O(n^2 + m*k)

 solution 3) dp

 let dp[i] true if possible to build s which length is i
 with segemented tokens

 build HashSet for tokens
 iterate i from 1 to n
 iterate j from 0 to i-1
 dp[i] = dp[j] & substr(j,i) presents // substr O(n)
 if true break;

 tc : O(n^3 + m*k)
 */
class Solution {
  public boolean wordBreak(String s, List<String> wordDict) {
    Set<String> dict = new HashSet<>(wordDict);
    boolean[] dp = new boolean[s.length() + 1];
    dp[0] = true;
    for(int i = 1; i < dp.length; i++) {
      for(int j = 0; j < i; j++) {
        if(dp[j] && dict.contains(s.substring(j, i))){
          dp[i] = true;
          break;
        }
      }
    }
    return dp[dp.length - 1];
  }
}


// class Solution1 {
//     public boolean wordBreak(String s, List<String> wordDict) {
//         Map<Character, List<String>> tokens = new HashMap<>();
//         for(String word : wordDict) {
//             tokens.putIfAbsent(word.charAt(word.length()-1), new ArrayList<>());
//             tokens.get(word.charAt(word.length()-1)).add(word);
//         }
//         boolean[] dp = new boolean[s.length()+1];
//         dp[0] = true;
//         for(int i = 1; i < dp.length; i++) {
//             List<String> token = tokens.get(s.charAt(i-1));
//             if(token == null) {dp[i] = false; continue;}
//             for(String word : token) {
//                 if(i - word.length() < 0) continue;
//                 dp[i] = dp[i-word.length()] && s.substring(i-word.length(), i).equals(word);
//                 if(dp[i]) break;
//             }
//         }
//         return dp[dp.length-1];
//     }
// }

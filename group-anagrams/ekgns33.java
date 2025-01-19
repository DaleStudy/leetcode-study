/**

 input : array of strings
 output : grouped anagrams

 ex) eat ate tea > same group

 solution 1) brute force
 ds : hashmap
 algo : sort
 generate Key by sorting string O(nlogn)

 save to hashmap

 tc : O(m* nlogn) when m is length of array, n is max length of string
 sc : O(m)

 solutino 2) better?
 cannot optimize m times read
 how about generating key

 sort = nlogn
 read = n << use frequency
 26 * n
 tc : O(m * (26 * n)) ~= O(mn)
 sc : O(m * 26) ~= O(m)
 */

class Solution {
  public List<List<String>> groupAnagrams(String[] strs) {
    Map<String, List<String>> map = new HashMap<>();
    int n = strs.length;
    for(String str : strs) {
      int l = str.length();
      char[] freq = new char[26];
      for(int i = 0; i < l; i++) {
        freq[str.charAt(i) - 'a']++;
      }
      String key = new String(freq);
      map.putIfAbsent(key, new ArrayList<>());
      map.get(key).add(str);
    }
    return List.copyOf(map.values());
  }
}

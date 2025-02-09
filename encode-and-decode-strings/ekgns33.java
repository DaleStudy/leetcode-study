class Solution {
  public String encode(List<String> strs) {
    StringBuilder res = new StringBuilder();
    for (String s : strs) {
      res.append(s.length()).append('|').append(s);
    }
    return res.toString();
  }


  /*
  * number + | + string
  * read number until |
  * move pointer, read substring
  *
  * tc : O(n) when n is the length of encoded string
  * sc : O(1)
  * */
  public List<String> decode(String str) {
    List<String> res = new ArrayList<>();
    int start = 0;
    while (start < str.length()) {
      int cur = start;
      //read until |
      while (str.charAt(cur) != '|') {
        cur++;
      }
      int length = Integer.parseInt(str.substring(start, cur));
      start = cur + 1;
      cur = start + length;
      res.add(str.substring(start, cur));
      start = cur;
    }
    return res;
  }
}

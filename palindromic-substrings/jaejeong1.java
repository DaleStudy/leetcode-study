class SolutionPalindromicSubstrings {
  // 1번쨰 풀이: 구현해야할 로직을 팰린드롬 여부 검사와 검사할 대상 문자열을 구하는 로직 둘로 나눈다
  // 팰린드롬 여부 검사: 투포인터 사용, lt=0, rt=length-1 로 시작해 동등성 여부를 검사
  // 시간복잡도: O(N), 공간복잡도: O(1)
  // 대상 문자열 구하기: 투포인터 사용. rt가 length보다 같거나 작을떄까지 계속 증가시키고,
  // rt가 끝에 도달하면 lt를 증가시키고, rt를 lt+1로 만든다. 모든 과정에서 팰린드롬 여부를 검사한다
  // 시간복잡도: O(N), 공간복잡도: O(1)
  // 결과
  // 시간복잡도: O(N^2), 공간복잡도: O(1)

  public int countSubstrings(String s) {
    var subStrings = s.toCharArray();

    if (subStrings.length == 0) return 0;
    if (subStrings.length == 1) return 1;

    var answer = 0;

    var lt = 0;
    var rt = 1;
    while(lt < subStrings.length){
      if (isPalindrome(s.substring(lt, rt))) {
        answer++;
      }

      if (rt <= subStrings.length-1){
        rt++;
      } else {
        lt++;
        rt = lt+1;
      }
    }

    return answer;
  }

  private boolean isPalindrome(String s) {
    var chars = s.toCharArray();
    var lt = 0;
    var rt = chars.length - 1;

    while(lt < rt) {
      if (chars[lt] != chars[rt]) {
        return false;
      }
      lt++;
      rt--;
    }

    return true;
  }
}

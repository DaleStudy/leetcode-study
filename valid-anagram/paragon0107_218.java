import java.util.Arrays;
/*
*  시간 복잡도:
*       toCharArray는 O(1)의 복잡도를 갖고 ArraySor의 경우 평균O(nlogn), 최악O(n^2)를 갖음(코테시 몇으로 계산하고 진행해야 할 지는 잘 모르겠네요..)
*  공간 복잡도:
*       s와t를 사용해서 그대로 배열로 만들기 때문에 O(n)
*
*
* */
class Solution {
    public static boolean isAnagram(String s, String t) {
        char[] s1 = s.toCharArray();
        char[] s2 = t.toCharArray();
        Arrays.sort(s1);
        Arrays.sort(s2);
        return Arrays.equals(s1, s2);
    }
}
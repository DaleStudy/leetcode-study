/**
    HashSet과 substring을 이용하여 문자열을 비교하면서 가능한 조합의 수를 누적하는 방식
    문자열 S 의 길이 -> N
    시간 복잡도 : O(N^2)
    공간 복잡도 : O(N)
 */
class Solution2 {
    Set<String> numberSet = new HashSet<>();
    {
        numberSet.addAll(Arrays.asList("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"));
    }
    public int numDecodings(String s) {
        if(s.length() == 1) return s.charAt(0) == '0' ? 0 : 1;
        
        int[] list = new int[s.length()];
        list[0] = isImpossibleDecode(s.substring(0,1)) ? 0 : 1;
        list[1] = isImpossibleDecode(s.substring(0,2)) ? 0 : 1;
        list[1] += list[0]==1 && !isImpossibleDecode(s.substring(1,2)) ? 1 : 0;
        

        for(int i = 2; i < s.length() ; i++) {
            list[i] += isImpossibleDecode(s.substring(i-1,i+1)) ? 0 : list[i-2];
            list[i] += isImpossibleDecode(s.substring(i,i+1)) ? 0 : list[i-1];
        }

        return list[s.length()-1];

    }

    public boolean isImpossibleDecode(String target) {
        int len = target.length();
        if(!numberSet.contains(target)) {
            return true;
        }

        return false;

    }
}

/**
    이전 substring() 연산 부분 최적화
    이전 substring()으로 문자열을 자르지 않고, charAt()을 이용하여 직접 연산하여 조합의 수를 누적시키는 방식
    문자열 S 의 길이 -> N
    시간 복잡도 : O(N)
    공간 복잡도 : O(N)
 */
class Solution {

    public int numDecodings(String s) {
        if(s.length() == 1) return s.charAt(0) == '0' ? 0 : 1;
        
        int[] list = new int[s.length()];
        list[0] = s.charAt(0) == '0' ? 0 : 1;
        int target = (s.charAt(0) - '0') * 10 + (s.charAt(1) - '0');
        list[1] = (target >= 10) && (target <= 26) ? 1 : 0;
        list[1] += list[0]==1 && s.charAt(1) != '0' ? 1 : 0;
        

        for(int i = 2; i < s.length() ; i++) {
            target = (s.charAt(i-1) - '0') * 10 + (s.charAt(i) - '0');
            list[i] += (target >= 10) && (target <= 26) ? list[i-2] : 0;
            list[i] += s.charAt(i) != '0' ? list[i-1] : 0;
        }

        return list[s.length()-1];

    }
}

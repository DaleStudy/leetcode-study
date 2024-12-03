import java.util.*;
class SolutionGotprgmer {
    // 해당 문제는 어느 한 숫자가 2개이상 존재할 경우 true를 그렇지 않을 경우, false를 반환하는 문제이다.
    // set을 사용해서 set에 이미 값이 존재한다면 개수가 2 이상이므로 true 그렇지 않으면 false를 출력한다.

    // 각 숫자들을 저장해서 set으로 관리 -> distinctNums
    // nums의 각 숫자인 checkNum을 distinctNums에 넣어준다.
    // 만약 checkNum이 이미 distinctNums에 존재한다면 ans를 true로 만들어주고 답을 출력한다.


    // 시간복잡도 -> O(n)
    // 공간복잡도 -> O(n)
    static Set<Integer> distinctNums;
    public boolean containsDuplicate(int[] nums) {
        distinctNums = new HashSet<>();
        boolean ans = false;
        for(int checkNum:nums){
            if(distinctNums.contains(checkNum)){
                ans = true;
                break;
            };
            distinctNums.add(checkNum);
        }
        return ans;
    }
    public static void main(String[] args){
        Solution s = new Solution();
        System.out.println(s);

    }


}
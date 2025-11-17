
import java.util.HashSet;
import java.util.Set;
/**
 각 연속 수열의 시작점에서만 카운팅하기

 1. 모든 숫자를 Set에 넣기
 2. 배열을 탐색하면서 현재 index에 해당하는 숫자 -1 값이 Set에 존재하는지 확인
 3. 만약 Set에 값이 존재한다면 연속된 숫자의 시작지점이 아니다.
 4. 만약 Set에 값이 존재하지 않는다면 연속된 숫자의 시작지점이다.
 5. 시작지점을 찾았으면 num + 1값이 존재하는지 확인, num+2값이 존재하는지 확인하면서 등장하지 않을때 까지 체크하고 길이를 최대 길이와 비교한다. (이때 배열을 기준으로 탐색하면 배열에 중복 숫자가 있을경우 매번 중복숫자에 대해서 length를 체크해야하므로 Set이 이득임)
 */
class sangyyypark {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i =  0; i < nums.length; i++) {
            int num = nums[i];
            set.add(num);
        }
        int max = 0;

        for(int num : set) {
            if(set.contains(num-1)) {
                continue;
            }
            int index = 1;
            int length = 1;
            while(set.contains(num+index)) {
                index++;
                length++;
            }
            max = Math.max(max,length);
        }
        return max;
    }
}


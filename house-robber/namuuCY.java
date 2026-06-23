class Solution {
/*

문제 이해
1. 1자로 주욱 나열되어있는 집 : 인접한다는 것은 index가 1차이 난다는 것
2. 인접하는 두 집을 연속해서 털면 안된다.
3. 2의 제약조건을 가지고 털 수 있는 돈의 최대 합

문제 해결을 위한 의식의 흐름
- 이거 예전에 백준에서 봤던 문제같음.
- 어떤 한 집을 방문할 때, 앞 집이 털렸을 경우와 털리지 않았을 경우를 모두 고려해야함.
- 맨 처음으로 DP를 생각하게 됨.
    - 털렸을 경우와 털리지 않았을 경우의 값을 모두 저장해놔야 할 것으로 생각
    - 2차원 배열 DP를 아래와 같이 정의한다면
    - DP[0-안털었다 or 1-털었다][index] = index번째 집까지 왔을때 훔친 돈의 총합
        1. 총합이므로 자료형은 int 만으로 충분? long 배열써야하는지?
            - nums[i]가 최대 400이고, nums 길이가 100 이하 이므로 int로도 충분
        2. DP 채워지는건 어떻게? 점화식
            - i번째 집을 방문할 때
                - i번째 집을 턴다고 가정 : i - 1 번째 집은 털지 않은 상태 + 현재 집의 돈
                - i번째 집을 털지 않는다고 가정 : i - 1 번째 집은 털어도 되고, 털지 않아도 됨 두 개중 최댓값
        3. 이렇게 DP를 정의할 경우, DAG인가?
            - i번째 집의 정보는 i-1번째 집의 정보로부터만 오기 때문에 DAG이다.
    - 엣지케이스? :
        - 맨 처음 index
        DP[0][0] = 0 / 0이면 더하지 않고,
        DP[0][0] = nums[0] / 1이면 더한다
        - 길이가 1이면?
- 쓰다보니 느낀건데 어차피 이전 집의 값만 필요하니까 굳이 DP를 사용안해도 될 것 같은데?
    - 이렇게 하면 array 로 데이터 저장할 필요 X


시공간복잡도
N : nums의 길이
- DP 풀이 :
    - 시간 복잡도 : O(N)
    - 공간 복잡도 : O(N) // N * 2 개만큼 저장해야함.
- DP X 풀이 :
    - 시간 복잡도 : O(N)
    - 공간 복잡도 : O(1) // 이전 값 2개만 저장하면 됨.

*/

/* DP 풀이
    public int rob(int[] nums) {
        int[][] DP = new int[2][nums.length];
        DP[1][0] = nums[0];

        for (int idx = 1 ; idx < nums.length; idx ++) {
            DP[1][idx] = DP[0][idx - 1] + nums[idx];
            DP[0][idx] = Math.max(DP[0][idx - 1], DP[1][idx - 1]);
        }

        return Math.max(DP[0][nums.length - 1], DP[1][nums.length - 1]);
    }
*/

	// DP X, 일반 순회 풀이
	public int rob(int[] nums) {
		int robbed = 0;
		int unrobbed = 0;

		int prevRobbed;
		int prevUnrobbed;

		for (int money : nums) {
			prevRobbed = robbed; // 0 1 2 4
			prevUnrobbed = unrobbed; // 0 0 1 2

			robbed = prevUnrobbed + money; // 1 2 4 3
			unrobbed = Math.max(prevUnrobbed, prevRobbed); // 0 1 2 4
		}

		return Math.max(robbed, unrobbed);
	}
}

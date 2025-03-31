class Solution {

    // 전문적인 강도인 당신은 거리에 있는 집들을 털 계획을 세우고 있다. 
    // 조건: 인접한 집들은 연결된 보안 경비 시스팀이 있어 인접한 집을 같은 날에 털 경우 자동적으로 경찰에 연락이 간다.
    // 각 집에 쌓아둔 돈의 양 배열 (정수 배열)이 주어질 때 경찰한테 걸리지 않고 털 수 있는 최대 돈의 양을 반환하시오.
    public int rob(int[] nums) {

        // 조건: 1 == nums.length (털 집이 한 곳 뿐)
        if (nums.length == 1) {
            return nums[0];
        }

        // DP로 계산
        nums[1] = Math.max(nums[0], nums[1]);

        for (int i = 2; i < nums.length; i++) {
            nums[i] = Math.max(nums[i - 1], nums[i - 2] + nums[i]);
        }

        return nums[nums.length - 1];

    }

}


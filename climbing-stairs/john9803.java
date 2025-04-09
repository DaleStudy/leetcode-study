import java.math.BigInteger;

// 1, 2 걸음으로 n개의 계단을 올라가는 방법의 가짓수를 계산

// ================================================================================
//  * 풀이 1 *
// ================================================================================
// n <= 45 이므로 최대한 2로 나눠서 가짓수 구하기
// n이 커짐에 따라서 계산의 범위가 굉장히 늘어남.
// 계산범위 초과로 풀이 실패.

// ================================================================================
// * 풀이 2 *
// ================================================================================
// 풀이 1을 보완한 풀이
// 단순히 조합 구현말고 다른 해결방안이 필요함 -> BigInteger로 계산범위 늘림.
// 풀이성공 -> 다만 런타임 시간이 평균풀이보다 너무 길고, 메모리 사용이 높아서 새로운 풀이 생각해봄.

// ================================================================================
// * 풀이 3 *
// ================================================================================
// 더 빠른 풀이를 위해서 찾아보던 중. n이 커짐에 따라서 나오는 값들의 규칙이 피보나치 배열임을 발견.
// f(n) = f(n-1) + f(n-2) 임을 이용해서 빠르게 풀이.
// 시간복잡도 = O(n)

class john9803 {
    public int climbStairs(int n) {
        // return firstApproch(n);
        // return bigIntSolve(n);
        return piboSolve(n);
    }

    public int firstApproch(int n){
        int result = 0;
        // 2걸음 최대한 들어가고 남은데 1로 채워넣는 걸로 가짓수 세기
        for(int step=0; 2*step<=n; step++){
            // 2걸음과 1은 순서를 가짐
            int totalNumCnt = step + (n-(2*step));
            // (totalNumCnt)C(step) -> Combination 을 계산해서 result에 더함
            int top = 1;
            int bottom = 1;
            // 처음에는 분자분모를 int로 놓았다가 분자계산에서 int범위를 벗어남.
            for(int c =0; c< step; c++){
                top *= (totalNumCnt-c);
                bottom *= (step-c);
            }
            result = result + (int)(top/bottom);
            // System.out.println("top: "+ top + " bottom: " + bottom + " step is: " + step +" result is: "+ result);
        }
        return result;
    }


    // 단순한 재귀를 통한 문제풀이
    // 문제가 생겼던 부분 n이 커짐에 따라서 계산범위가 커졌음.
    // 따라서 결과적으로 계산이 가능하게끔 메모리를 크게 부여하는 BigInteger를 사용하는 방법으로 풀이
    public int bigIntSolve(int n){
        int result = 0;

        for(int step=0; 2*step<=n; step++){
            int totalNumCnt = step + (n-(2*step));
            // (totalNumCnt)C(step) -> Combination 을 계산해서 result에 더함
            BigInteger top = new BigInteger("1");
            BigInteger bottom = new BigInteger("1");

            for(int c =0; c< step; c++){
                top = top.multiply(new BigInteger(String.valueOf(totalNumCnt-c)));
                bottom = bottom.multiply(new BigInteger(String.valueOf(step-c)));
            }
            result += (top.divide(bottom)).intValue();
            // System.out.println("top: "+ top + " bottom: " + bottom + " step is: " + step +" result is: "+ result);
        }
        return result;
    }

    // n이 커짐에 따라서 값이 피보나치 수열의 규칙성을 지니는 것을 파악함.
    // 풀이를 피보나치 수열을 이용해 풀이 하도록 구현
    // f(n) = f(n-1) + f(n-2) 임을 이용.
    public int piboSolve(int n){
        int prev = 1;
        int curr = 1;

        for(int i=2; i<=n; i++){
            int temp = prev+curr;
            prev = curr;
            curr = temp;
        }
        return curr;
    }

}

/**
 * 대표적인 조건 기반 마킹 문제: 조건을 만족하면 바로 바꾸지 않고, 먼저 표시만 해두고 마지막에 한번에 처리하는 기법
 * 보조 배열을 쓰는 방식이면 2번 전체 탐색이 기본이다.
 */

/**
 * 매트릭스 문제 유형을 알고 easy와 연관 유형을 선행한 다음에 정답을 맞출 수 있었다.
 * 1. 조건 기반 갱신/마킹
 * 2. 이웃 집계
 * 3. 행렬 변형
 * 4. 단순 순회
 */
class Solution {
    public void setZeroes(int[][] matrix) {
        int[][] assist = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    for (int ni = 0; ni < matrix.length; ni++) {
                        assist[ni][j] = -1;
                    }

                    for (int nj = 0; nj < matrix[0].length; nj++) { // 범위 확인 잘하기
                        assist[i][nj] = -1;
                    }
                }
            }
        }

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                // assist[i][j]가 -1이면 0으로 바꾼다.
                if (assist[i][j] == -1) {
                    matrix[i][j] = 0;
                }
            }
        }
    }

    /**
     * 선행 문제들을 모두 풀면 반복할 부분과 응용할 부분을 분리할 수 있었고, 그 부분을 계속 반복학습한 다음에 떼어내서 변형을 시도했다.
     */
    // 2차원 그리드의 기초 문제 - 행 단위 합산 후 최대값 찾기
    // https://leetcode.com/problems/richest-customer-wealth/
    public int maximumWealth(int[][] accounts) {
        int maxW = 0;
        for (int i = 0; i < accounts.length; i++) {
            int current = 0;
            for (int j = 0; j < accounts[0].length; j++) {
                current += accounts[i][j];
            }
            maxW = Math.max(maxW, current);
        }
        return maxW;
    }

    // 여기서 invert란 row마다 역순 정렬을 1번 하고, 다시 for문으로 0은 1로, 1은 0으로 바꾸는 것을 의미한다.
    // https://leetcode.com/problems/flipping-an-image/
    public int[][] flipAndInvertImage(int[][] image) {
        for (int i = 0; i < image.length; i++) {
            int left = 0;
            int right = image[0].length - 1;

            while (left < right) {
                int temp = image[i][left];
                image[i][left] = image[i][right];
                image[i][right] = temp;

                right--;
                left++;
            }
        }

        for (int i = 0; i < image.length; i++) {
            for (int j = 0; j < image[0].length; j++) {
                image[i][j] = image[i][j] == 0 ? 1 : 0;
            }
        }
        return image;
    }

    // grid[i][j]를 grid[j][i]로 바꾸는 문제. grid[2][3] -> grid[3][2] 이중 for문을 어떻게 반영할까? 처음에는 생각이 안 나서 while + for로 했다가 이중 for문으로 작은 리팩토링
    // https://leetcode.com/problems/transpose-matrix/description/
    public int[][] transpose(int[][] matrix) {
        int[][] answer = new int[matrix[0].length][matrix.length];

        for (int j = 0; j < matrix[0].length; j++) {
            for (int i = 0; i < matrix.length; i++) {
                answer[j][i] = matrix[i][j];
            }
        }
        return answer;
    }

    // 8방향을 도전, dir 배열이 틀리지 않게 하는 게 어려웠다. -> 범위를 벗어났는 지 확인하는 로직이 마치 dfs의 그것이었다. (0보다 작은지, length보다 크거나 같은지 국룰 확인)
    // 여기서 알아야 할 점은 입력받은 배열을 수정하는 경우와 assist 배열이 꼭 필요한 경우를 구분해야 한다는 것이다.
    // 이 문제는 [i][j]마다 평균을 계산하지만 원본 배열을 바꾸지 않고 assist에 기록한 다음에 그걸 반환해야 한다. (계산은 매번 입력받은 데이터로 하기 때문이다)
    // https://leetcode.com/problems/image-smoother/
    public int[][] imageSmoother(int[][] img) {
        int[][] dir8 = new int[][]{
                {-1, 0},
                {-1, 1},
                {0, 1},
                {1, 1},
                {1, 0},
                {1, -1},
                {0, -1},
                {-1, -1}
        };

        int[][] assist = new int[img.length][img[0].length];

        for (int i = 0; i < img.length; i++) {
            for (int j = 0; j < img[0].length; j++) {
                // dir의 8을 돌리는데 중요한 건 sum, cnt가 칸마다 다르다는 것이다. 그래서 평균을 /8이 아니라 /cnt로 하고 sum도 마찬가지였다.
                int sum = img[i][j];
                int cnt = 1;
                for (int[] d : dir8) { // 3중 for문 안에서 ni, nj 개념을 setMatrixZeros에서 썼다.
                    int ni = i + d[0];
                    int nj = j + d[1];

                    if (ni < 0 || ni >= img.length || nj < 0 || nj >= img[0].length) { // 범위를 벗어나면 넘어가는 로직을 참고했다.
                        continue;
                    }

                    sum += img[ni][nj];
                    cnt++;
                }
                assist[i][j] = sum / cnt;
            }
        }
        return assist;
    }

    //
    // https://leetcode.com/problems/game-of-life/
}

import java.util.*;


class Solution {

    //상,하,좌,우
    static int[] dx = {0,1,-1,0};
    static int[] dy = {1,0,0,-1};

    static int m, n;

    static boolean result; //exist 함수가 호출될때마다 초기화해야함
    static char[][] map; //지역변수 board 저장용
    static String w; //word 저장용
    public boolean exist(char[][] board, String word) {

        result=false;

        m = board.length;
        n = board[0].length;

        w = word;
        //map <- board
        map = new char[m][n];
        for(int i =0; i<m;i++){
            for(int j=0; j< n; j++){
                map[i][j] = board[i][j];
            }
        }


        for(int x =0 ; x < m; x++){
            for(int y =0 ; y < n ;y++){
                dfs(x, y , 0); //위치 x,y, word에 대한 찾는 인덱스
                if (result) return result;
            }
        }



        //기본 
        return result;
    }

    private static void dfs(int x, int y, int idx){
        //종료조건
        if (result) return;

        if (!checkin(x, y) || map[x][y] != w.charAt(idx)) return;

        //마지막 문자일때 종료
        if (idx == w.length() - 1){
            result = true;
            return;
        }   

        char temp = map[x][y];
        map[x][y] = '#';

        for(int i = 0; i < 4; i++){
            dfs(x + dx[i], y + dy[i], idx + 1);
        }

        map[x][y] = temp;
            
    }

    //map 내부 checkin 함수 정의
    private static boolean checkin(int x, int y){
        return x >= 0 && x < m && y >= 0 && y < n;
    }
}


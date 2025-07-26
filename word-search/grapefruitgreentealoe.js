/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    //word를 순회해서 board의 x,y를 조절하여, 값이 있으면 계속 true
    const xLength = board[0].length;
    const yLength = board.length

    // 체크 배열: 방문 여부를 저장. 각 DFS마다 새로 초기화될 필요는 없음 (DFS 내에서 백트래킹 처리하므로)
    const check = Array.from({ length: yLength }, () => Array(xLength).fill(false));


    // 단어의 첫 글자와 일치하는 시작점을 모두 수집
    const startPoints = []
    for(let i = 0; i<xLength;i++){
        for(let j = 0; j<yLength;j++){
            if(board[j][i] == word[0]){
                startPoints.push([j,i])
            }
        }
    }
    // 각 시작점에서 DFS 시도
    for(let startPoint of startPoints){
        // 잘못된 길로 가는 경우도 있기 때문에 백트렉킹은 무조건 필요하다. 
        if(backTracking(startPoint,board,word,check)) return true
    }

    return false
};

function backTracking(startPoint,board,word,check){
    const xLength = board[0].length;
    const yLength = board.length
    const upDownLeftRight = [[-1,0],[1,0],[0,-1],[0,1]]
    //스타트 포인트부터 해서, 완성이 가능한지를 dfs를 통해서 진행한다. 
    //idx는 현재 확인해야할 word의 idx이다. 
    function dfs(y,x,idx){
        if(idx == word.length) return true
        
        if(y < 0 || y >= yLength ||
           x < 0 || x >= xLength  || 
           check[y][x] ||
           board[y][x] !== word[idx]
        ) return false;

        check[y][x] = true
        // 4방향 탐색
        for(let [dy,dx] of upDownLeftRight){
            //만약 타겟에 해당하는지를 확인을 먼저 해야할것같음!
            if(dfs(y+dy,x+dx,idx+1)) return true //4방향에 대해서 모두 dfs를 진행한다.
            
        }

        //백트레킹
        check[y][x] = false;
        return false
        
    }
    return dfs(...startPoint,0)
}
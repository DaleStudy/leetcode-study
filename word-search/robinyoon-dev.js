/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function (board, word) {

    let tempResult = false;

    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === word[0]) {
                tempResult = dfs(i, j, 0);
                if (tempResult) {
                    return true;
                }
            } else {
                continue;
            }
        }
    }


    return tempResult;



    function dfs(x, y, currentIndex) {

        if (x < 0 || y < 0 || x >= board.length || y >= board[0].length) {
            return false;
        }

        if (board[x][y] !== word[currentIndex]) {
            return false;
        }

        let nextIndex = currentIndex + 1;

        if (nextIndex === word.length) {
            return true;
        }

        let tempChar = board[x][y];
        board[x][y] = '*';


        let hasCharOnTheLeft = dfs(x - 1, y, nextIndex);
        let hasCharOnTheRight = dfs(x + 1, y, nextIndex);
        let hasCharAtTheTop = dfs(x, y + 1, nextIndex);
        let hasCharAtTheBottom = dfs(x, y - 1, nextIndex);

        board[x][y] = tempChar;

        return hasCharOnTheLeft || hasCharOnTheRight || hasCharAtTheTop || hasCharAtTheBottom;
    }
};

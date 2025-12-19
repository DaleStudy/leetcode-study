function spiralOrder(matrix: number[][]): number[] {
    let x = 0;
    let y = 0;

    let result: number[] = [];
    const threshold = matrix.length * matrix[0].length

    let direction = 0;
    const dx = [0, 1, 0, -1];
    const dy = [1, 0, -1, 0];
    let visited = Array.from({ length: matrix.length }, () => Array(matrix[0].length).fill(false))

    while (true) {
        if (result.length >= threshold) {
            break;
        }

        result.push(matrix[x][y]);
        visited[x][y] = true

        const nx = x + dx[direction]
        const ny = y + dy[direction]

        if (nx < 0 || nx >= matrix.length || ny < 0 || ny >= matrix[0].length || visited[nx][ny]) {
            direction++;
            
            if (direction > 3) {
                direction = 0;
            }

            x += dx[direction];
            y += dy[direction];
        } else {
            x = nx;
            y = ny;
        }
    }

    return result;
};

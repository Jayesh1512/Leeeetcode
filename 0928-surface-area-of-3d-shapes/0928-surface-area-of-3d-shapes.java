class Solution {
    public int surfaceArea(int[][] grid) {
        int sum = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int h = grid[i][j];
                int fullS = h > 0 ? h * 4 + 2 : 0;
                //check adjacent and substract touching surface
                //check left
                if (cellExists(i, j - 1, grid)) {
                    if (h <= grid[i][j - 1]) {
                        fullS -= h;
                    } else {
                        fullS -= grid[i][j - 1];
                    }
                }
                //check up
                if (cellExists(i - 1, j, grid)) {
                    if (h <= grid[i - 1][j]) {
                        fullS -= h;
                    } else {
                        fullS -= grid[i - 1][j];
                    }
                }
                //check right
                if (cellExists(i, j + 1, grid)) {
                    if (h <= grid[i][j + 1]) {
                        fullS -= h;
                    } else {
                        fullS -= grid[i][j + 1];
                    }
                }
                //check down
                if (cellExists(i + 1, j, grid)) {
                    if (h <= grid[i + 1][j]) {
                        fullS -= h;
                    } else {
                        fullS -= grid[i + 1][j];
                    }
                }
                sum += fullS;
            }
        }
        return sum;
    }

    private static boolean cellExists(int row, int col, int[][] array) {
        return (row <= array.length - 1 && row >= 0) && (col <= array[0].length - 1 && col >= 0);
    }
}
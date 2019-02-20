package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public int uniquePathsWithObstacles(int[][] obstacleGrid) {
            Integer[][] dp = new Integer[obstacleGrid.length][obstacleGrid[0].length];
            return uniquePathsWithObstacles(obstacleGrid, dp, 0, 0);
        }

        public int uniquePathsWithObstacles(int[][] obstacleGrid, Integer[][] dp, int x, int y) {
            if (x >= dp.length || y >= dp[0].length) {
                return 0;
            }
            if (obstacleGrid[x][y] == 1) {
                return 0;
            }
            if (x == dp.length - 1 && y == dp[0].length - 1) {
                return 1;
            }
            if (dp[x][y] != null) {
                return dp[x][y];
            }
            int result = uniquePathsWithObstacles(obstacleGrid, dp, x + 1, y) + uniquePathsWithObstacles(obstacleGrid, dp, x, y + 1);
            dp[x][y] = result;
            return result;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().uniquePathsWithObstacles(new int[][]{
                {0, 0, 0},
                {0, 1, 0},
                {0, 0, 0}}
        ));
    }

}


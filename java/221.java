package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * DP
     * 创建tmp数组，用于纪录对应格子的边长(当前格子作为正方形的右下角)
     */
    class Solution {
        public int maximalSquare(char[][] matrix) {
            if (matrix == null || matrix.length == 0) {
                return 0;
            }
            int maxSize = 0;
            int line = matrix.length;
            int column = matrix[0].length;
            int[][] tmp = new int[line + 1][column + 1];
            for (int i = 1; i <= line; i++) {
                for (int j = 1; j <= column; j++) {
                    if (matrix[i - 1][j - 1] == '0') {
                        continue;
                    }
                    tmp[i][j] = Math.min(tmp[i - 1][j - 1], Math.min(tmp[i - 1][j], tmp[i][j - 1])) + 1;
                    maxSize = Math.max(tmp[i][j], maxSize);
                }
            }
            return maxSize * maxSize;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1', '0'}
        }) + " 4");
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'0', '0', '0'},
                {'0', '0', '0'},
                {'0', '0', '0'},
                {'0', '0', '0'}
        }) + " 0");
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'0', '0', '0', '1'},
                {'1', '1', '0', '1'},
                {'1', '1', '1', '1'},
                {'0', '1', '1', '1'},
                {'0', '1', '1', '1'}
        }) + " 9");
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'0', '1'}
        }) + " 1");
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'1'}
        }) + " 1");
        System.out.println(new Algorithm().new Solution().maximalSquare(new char[][]{
                {'0'}
        }) + " 0");
    }

}


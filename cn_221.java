package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 创建tmp数组，用于纪录对应格子的边长(当前格子作为正方形的右下角)
     * 初始化，先将'1'的格子对应的边长设置为0
     * 然后遍历原始数组，判断当前遍历的点的左上角对角线的那个格子是否构成正方形
     * 如果构成正方形的话，先将边长设置为左上角对角线的格子的正方形的边长+1
     * 然后判断新的边长是否满族要求（也就是判断横向和竖向两条线是否都是1）
     * 如果不满足，就减少边长，然后重试
     */
    class Solution {
        public int maximalSquare(char[][] matrix) {
            if (matrix == null || matrix.length == 0) {
                return 0;
            }
            int maxSize = 0;
            int line = matrix.length;
            int column = matrix[0].length;
            int[][] tmp = new int[line][column];
            boolean[][] cache = new boolean[line][column];
            for (int i = 0; i < line; i++) {
                for (int j = 0; j < column; j++) {
                    tmp[i][j] = (int) matrix[i][j] - (int) '0';
                }
            }
            for (int i = 0; i < line; i++) {
                for (int j = 0; j < column; j++) {
                    if (cache[i][j]) {
                        continue;
                    }
                    cache[i][j] = true;
                    if (i == 0 || j == 0) {
                        maxSize = Math.max(maxSize, tmp[i][j]);
                        continue;
                    }
                    if (tmp[i - 1][j - 1] == 0) {
                        continue;
                    }
                    // 上一个节点正好是正方形的右下角
                    int newSize = tmp[i - 1][j - 1] + 1;
                    while (newSize > 0) {
                        if (check(matrix, i, j, newSize, cache)) {
                            tmp[i][j] = newSize;
                            maxSize = Math.max(maxSize, newSize);
                            break;
                        }
                        newSize--;
                    }
                }
            }
            return (int) Math.pow(maxSize, 2);
        }

        private boolean check(char[][] matrix, int i, int j, int size, boolean[][] cache) {
            for (int tmp = i; tmp > i - size; tmp--) {
                cache[tmp][j] = true;
                if (matrix[tmp][j] == '0') {
                    return false;
                }
            }
            for (int tmp = j; tmp > j - size; tmp--) {
                cache[i][tmp] = true;
                if (matrix[i][tmp] == '0') {
                    return false;
                }
            }
            return true;
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


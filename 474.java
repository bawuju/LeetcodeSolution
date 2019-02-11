package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {

        public int findMaxForm(String[] strs, int m, int n) {
            int[][][] dp = new int[strs.length + 1][m + 1][n + 1];
            for (int[][] ints : dp) {
                for (int[] anInt : ints) {
                    for (int i = 0; i < anInt.length; i++) {
                        anInt[i] = -1;
                    }
                }
            }
            return findMaxForm(strs, 0, m, n, dp, new int[strs.length + 1][2]);
        }

        public int findMaxForm(String[] strs, int index, int m, int n, int[][][] dp, int[][] countCache) {
            if (dp[index][m][n] >= 0) {
                return dp[index][m][n];
            }
            int result;
            if (index >= strs.length) {
                result = 0;
            } else {
                if (countCache[index][0] == 0 && countCache[index][1] == 0) {
                    int[] c = getCount(strs[index]);
                    countCache[index][0] = c[0];
                    countCache[index][1] = c[1];
                }
                int[] count = countCache[index];
                if (m >= count[0] && n >= count[1]) {
                    result = Math.max(findMaxForm(strs, index + 1, m, n, dp, countCache), 1 + findMaxForm(strs, index + 1, m - count[0], n - count[1], dp, countCache));
                } else {
                    result = findMaxForm(strs, index + 1, m, n, dp, countCache);
                }
            }
            dp[index][m][n] = result;
            return result;
        }

        private int[] getCount(String s) {
            int m = 0;
            int n = 0;
            for (char c : s.toCharArray()) {
                if (c == '0') {
                    m++;
                }
                if (c == '1') {
                    n++;
                }
            }
            return new int[]{m, n};
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().findMaxForm(new String[]{"10", "0001", "111001", "1", "0"}, 5, 3) + " 4");
        System.out.println(new Algorithm().new Solution().findMaxForm(new String[]{"10", "0", "1"}, 1, 1) + " 2");
        System.out.println(new Algorithm().new Solution().findMaxForm(new String[]{"10", "0001", "111001", "1", "0"}, 4, 3) + " 3");
        System.out.println(new Algorithm().new Solution().findMaxForm(new String[]{"101", "110", "0", "0", "0", "0001", "1010", "01", "10110", "0011", "0", "10", "11", "110", "1", "10", "0", "1", "00", "1", "0", "010", "1", "000", "0", "101", "0", "11", "1", "01111", "110000", "1", "01"}, 47, 88) + " 33");
    }

}


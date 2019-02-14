package com.bawuju.java.demo.pure;

import java.util.Arrays;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 动态规划
     * 注意0开头的是无效的（即无法完成解析）
     * 这里用-1表示无效
     * 如果当前位置截取1个或者2个都是-1，那么这个index的解析种类就是无效的
     */
    class Solution {
        public int numDecodings(String s) {
            int[] dp = new int[s.length()];
            Arrays.fill(dp, Integer.MIN_VALUE);
            return numDecodings(s, s.length() - 1, dp);
        }

        private int numDecodings(String s, int index, int[] dp) {
            if (index < 0) {
                return 1;
            }
            if (dp[index] != Integer.MIN_VALUE) {
                return dp[index];
            }
            int result;
            int twoCharInt = index > 0 ? Integer.valueOf(s.substring(index - 1, index + 1)) : Integer.MAX_VALUE;
            char oneCharFirst = s.charAt(index);
            char twoCharFirst = index > 0 ? s.charAt(index - 1) : '0' - 1;
            int r1 = oneCharFirst > '0' ? numDecodings(s, index - 1, dp) : -1;
            int r2 = twoCharFirst > '0' && twoCharInt <= 26 ? numDecodings(s, index - 2, dp) : -1;
            if (r1 == -1 && r2 == -1) {
                result = -1;
            } else {
                result = (r1 == -1 ? 0 : r1) + (r2 == -1 ? 0 : r2);
            }
            dp[index] = result;
            return index == s.length() - 1 && result == -1 ? 0 : result;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().numDecodings("12") + " 2");
        System.out.println(new Algorithm().new Solution().numDecodings("226") + " 3");
        System.out.println(new Algorithm().new Solution().numDecodings("01") + " 0");
    }

}


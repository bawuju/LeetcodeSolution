package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public int numTrees(int n) {
            return numTrees(n, new int[n + 1]);
        }

        public int numTrees(int n, int[] dp) {
            if (n <= 1) {
                return 1;
            }
            if (dp[n] > 0) {
                return dp[n];
            }
            int num = 0;
            for (int i = 0; i < n; i++) {
                num += (numTrees(i, dp) * numTrees(n - i - 1, dp));
            }
            dp[n] = num;
            return num;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().numTrees(3) + " 5");
    }

}


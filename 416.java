package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {

        public boolean canPartition(int[] nums) {
            int sum = 0;
            for (int num : nums) {
                sum += num;
            }
            if (sum % 2 != 0) {
                return false;
            }
            int target = sum / 2;
            boolean[][] dp = new boolean[nums.length + 1][target + 1];
            for (int i = 1; i < (nums.length + 1); i++) {
                int current = nums[i - 1];
                for (int j = 1; j < (target + 1); j++) {
                    if (current > j) {
                        dp[i][j] = dp[i - 1][j];
                    } else if (current < j) {
                        dp[i][j] = dp[i - 1][j] || dp[i - 1][j - current];
                    } else {
                        dp[i][j] = true;
                    }
                }
            }
            return dp[nums.length][target];
        }

    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().canPartition(new int[]{1, 5, 11, 5}));
        System.out.println(new Algorithm().new Solution().canPartition(new int[]{1, 2, 3, 5}));
        System.out.println(new Algorithm().new Solution().canPartition(new int[]{1, 2, 5}));
    }

}


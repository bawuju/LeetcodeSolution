package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 常规DP
     */
    class Solution {
        public int maxSubArray(int[] nums) {
            if (nums == null || nums.length == 0) {
                return 0;
            }
            int[] dp = new int[nums.length + 1];
            int max = Integer.MIN_VALUE;
            for (int i = 1; i <= nums.length; i++) {
                dp[i] = Math.max(nums[i - 1], nums[i - 1] + dp[i - 1]);
                max = Math.max(max, dp[i]);
            }
            return max;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().maxSubArray(new int[]{-2, 1, -3, 4, -1, 2, 1, -5, 4}) + " 6");
    }

}


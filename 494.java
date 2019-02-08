package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public int findTargetSumWays(int[] nums, int S) {
            return findTargetSumWays(nums, S, nums.length - 1);
        }

        private int findTargetSumWays(int[] nums, int S, int end) {
            if (end == 0) {
                return (nums[0] == S ? 1 : 0) + (nums[0] == -S ? 1 : 0);
            } else {
                return findTargetSumWays(nums, S - nums[end], end - 1) + findTargetSumWays(nums, S + nums[end], end - 1);
            }
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().findTargetSumWays(new int[]{1, 1, 1, 1, 1}, 3));
    }

}


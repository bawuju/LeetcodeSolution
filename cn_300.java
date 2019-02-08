package com.bawuju.java.demo.pure;

import java.util.Arrays;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 使用数组存储已经组合好的递增数列
     * 长度:结尾数字
     * 同一个长度之下，结尾数字越小越好
     * 当找到插入位置index（第一个大于key的位置）时，也就是说，从dp[index-1]开始构建，结尾加上当前数字，结尾数字应该存在dp[index]中
     * 而当前结尾数字num正好小于index，所以直接赋值dp[index]=num
     */
    class Solution {
        public int lengthOfLIS(int[] nums) {
            // 长度:结尾数字
            int[] dp = new int[nums.length];
            int maxLength = 0;
            for (int num : nums) {
                int index = Arrays.binarySearch(dp, 0, maxLength, num);
                // 已经找到，重复数字
                if (index >= 0) {
                    continue;
                }
                // 未找到，把index转化成插入位置（第一个大于key的位置）
                index = -index - 1;
                if (index == maxLength) {
                    dp[maxLength] = num;
                    maxLength += 1;
                } else {
                    dp[index] = num;
                }
            }
            return maxLength;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().lengthOfLIS(new int[]{10, 9, 2, 5, 3, 7, 101, 18}));
    }

}


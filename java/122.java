package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 经典贪心算法
     */
    class Solution {
        public int maxProfit(int[] prices) {
            int remain = 0;
            for (int i = 1; i < prices.length; i++) {
                if (prices[i] > prices[i - 1])
                    remain += prices[i] - prices[i - 1];
            }
            return remain;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().maxProfit(new int[]{7, 1, 5, 3, 6, 4}) + " 7");
        System.out.println(new Algorithm().new Solution().maxProfit(new int[]{1, 2, 3, 4, 5}) + " 4");
        System.out.println(new Algorithm().new Solution().maxProfit(new int[]{7, 6, 4, 3, 1}) + " 0");
    }

}


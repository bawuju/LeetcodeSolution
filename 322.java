package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {

        /**
         * 动态规划，完全背包问题（硬币可以重复）
         * 状态转移方程：最小硬币数量(金额为C)=最小金币数量-1(金额为C-i)
         */
        public int coinChange(int[] coins, int amount) {
            return coinChange(coins, amount, new int[amount + 1]);
        }

        public int coinChange(int[] coins, int amount, int dp[]) {
            if (amount == 0) {
                return 0;
            }
            if (dp == null) {
                dp = new int[amount + 1];
            }
            if (dp[amount] != 0) {
                return dp[amount];
            }
            int minCount = Integer.MAX_VALUE;
            for (int coin : coins) {
                if (coin > amount) {
                    continue;
                }
                if (coin == amount) {
                    minCount = 1;
                    break;
                }
                if (coin < amount) {
                    int count = coinChange(coins, amount - coin, dp) + 1;
                    if (count > 0) {
                        minCount = Math.min(count, minCount);
                    }
                }
            }
            dp[amount] = (minCount == Integer.MAX_VALUE ? -1 : minCount);
            return dp[amount];
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().coinChange(new int[]{1, 2, 5}, 11) + " 3");
        System.out.println(new Algorithm().new Solution().coinChange(new int[]{2}, 3) + " -1");
        System.out.println(new Algorithm().new Solution().coinChange(new int[]{186, 419, 83, 408}, 6249) + " 20");
    }

}


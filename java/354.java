package com.bawuju.java.demo.pure;

import java.util.Arrays;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public int maxEnvelopes(int[][] envelopes) {
            int max = 0;
            Arrays.sort(envelopes, (o1, o2) -> o1[0] != o2[0] ? o1[0] - o2[0] : o1[1] - o2[1]);
            int[] dp = new int[envelopes.length + 1];
            for (int i = 1; i <= envelopes.length; i++) {
                int last = 0;
                for (int j = i; j > 0; j--) {
                    if (envelopes[j - 1][0] < envelopes[i - 1][0] && envelopes[j - 1][1] < envelopes[i - 1][1]) {
                        last = Math.max(dp[j], last);
                    }
                }
                dp[i] = 1 + last;
                max = Math.max(dp[i], max);
            }
            return max;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().maxEnvelopes(new int[][]{{5, 4}, {6, 4}, {6, 7}, {2, 3}}));
        System.out.println(new Algorithm().new Solution().maxEnvelopes(new int[][]{{46, 89}, {50, 53}, {52, 68}, {72, 45}, {77, 81}}));
        System.out.println(new Algorithm().new Solution().maxEnvelopes(new int[][]{{10, 8}, {1, 12}, {6, 15}, {2, 18}}));
    }

}


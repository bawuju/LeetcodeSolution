package com.bawuju.java.demo.pure;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {


    /**
     * 使用单个长度为高度的数组
     * 三角形的高度即为最下面一层的长度
     * 每层的最小值数据，在遍历完之后就没用了
     * 所以可以用一个数组保存，一边遍历一边覆盖
     */
    class Solution {
        public int minimumTotal(List<List<Integer>> triangle) {
            int[] dp = new int[triangle.size() + 1];
            for (int i = triangle.size() - 1; i >= 0; i--) {
                for (int j = 0; j < triangle.get(i).size(); j++) {
                    dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(i).get(j);
                }
            }
            return dp[0];
        }
    }

    private static List<List<Integer>> array2List(int[][] nums) {
        List<List<Integer>> result = new LinkedList<>();
        for (int[] num : nums) {
            List<Integer> tmp = new LinkedList<>();
            result.add(tmp);
            for (int i : num) {
                tmp.add(i);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().minimumTotal(array2List(new int[][]{
                {2},
                {3, 4},
                {6, 5, 7},
                {4, 1, 8, 3}
        })));
    }

}


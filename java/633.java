package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    class Solution {
        public boolean judgeSquareSum(int c) {
            int base = (int) Math.sqrt(c);
            for (int i = base; i >= 0; i--) {
                double tmp = Math.sqrt(c - Math.pow(i, 2));
                if (tmp == (int) tmp) {
                    return true;
                }
            }
            return false;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().judgeSquareSum(5));
    }

}


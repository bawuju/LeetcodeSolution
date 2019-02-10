package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    /**
     * 二的指数都是10000
     * 减一就是1111
     * 与一下就是0
     */
    class Solution {
        public boolean isPowerOfTwo(int n) {
            return n > 0 && (n & (n - 1)) == 0;
        }
    }

    public static void main(String[] args) {

    }

}


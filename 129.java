package com.bawuju.java.demo.pure;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    class Solution {

        private int sum = 0;

        public int sumNumbers(TreeNode root) {
            sumNumbers(root, 0);
            return sum;
        }

        public void sumNumbers(TreeNode root, int lastSum) {
            if (root == null) {
                return;
            }
            int currentSum = lastSum * 10 + root.val;
            if (root.left == null && root.right == null) {
                sum += currentSum;
            } else {
                sumNumbers(root.left, currentSum);
                sumNumbers(root.right, currentSum);
            }
        }

    }

    public static void main(String[] args) {

    }

}


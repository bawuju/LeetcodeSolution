package com.bawuju.java.demo.pure;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by bawuju on 19-2-2.
 * Email: bawuju@gmail.com
 */
public class Algorithm {

    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    class Solution {
        private Map<TreeNode, Integer> dp = new HashMap<>();

        public int maxPathSum(TreeNode root) {
            if (root == null) {
                return Integer.MIN_VALUE;
            }
            int rootPathSum = Math.max(maxPath(root.left), 0) + Math.max(maxPath(root.right), 0) + root.val;
            int childPathSum = Math.max(maxPathSum(root.left), maxPathSum(root.right));
            return Math.max(rootPathSum, childPathSum);
        }

        private int maxPath(TreeNode root) {
            if (root == null) {
                return Integer.MIN_VALUE;
            }
            if (dp.containsKey(root)) {
                return dp.get(root);
            }
            int childMaxPath = Math.max(maxPath(root.left), maxPath(root.right));
            int path = root.val + Math.max(0, childMaxPath);
            dp.put(root, path);
            return path;
        }
    }

    public static void main(String[] args) {
        System.out.println(new Algorithm().new Solution().maxPathSum(new TreeNode(-3)));
    }

}


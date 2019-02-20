class Solution {

    public String getPermutation(int n, int k) {
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = i + 1;
        }
        return getPermutation(nums, k).toString();
    }

    private StringBuilder getPermutation(int[] nums, int k) {
        StringBuilder builder = new StringBuilder();
        if (k == 0) {
            for (int i = nums.length - 1; i >= 0; i--) {
                builder.append(nums[i]);
            }
        } else {
            int count = 1;
            for (int i = 1; i < nums.length; i++) {
                count *= i;
            }
            int targetIndex = k % count == 0 ? k / count - 1 : k / count;
            builder.append(nums[targetIndex]);
            int[] newNums = new int[nums.length - 1];
            int j = 0;
            for (int i = 0; i < nums.length; i++) {
                if (i != targetIndex) {
                    newNums[j] = nums[i];
                    j++;
                }
            }
            builder.append(getPermutation(newNums, k % count));
        }
        return builder;
    }

}

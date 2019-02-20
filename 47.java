class Solution {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums.length == 1) {
            result.add(Collections.singletonList(nums[0]));
            return result;
        }
        Arrays.sort(nums);
        int last = Integer.MIN_VALUE;
        for (int num : nums) {
            if (last == num) {
                continue;
            }
            last = num;
            List<List<Integer>> nextResult = permuteUnique(getRemainArray(nums, num));
            for (List<Integer> list : nextResult) {
                List<Integer> tmp = new ArrayList<>(list);
                tmp.add(num);
                result.add(tmp);
            }
        }
        return result;
    }

    private int[] getRemainArray(int[] nums, int except) {
        int[] newArray = new int[nums.length - 1];
        int index = 0;
        boolean deal = false;
        for (int num : nums) {
            if (num == except && !deal) {
                deal = true;
                continue;
            }
            newArray[index] = num;
            index++;
        }
        return newArray;
    }

}

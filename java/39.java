class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        combinationSum(candidates, target, result, new int[candidates.length], 0);
        return result;
    }

    private void combinationSum(int[] candidates, int target, List<List<Integer>> result, int[] tmp, int startIndex) {
        if (target == 0) {
            List<Integer> subResult = new ArrayList<>();
            for (int i = 0; i < tmp.length; i++) {
                for (int j = 0; j < tmp[i]; j++) {
                    subResult.add(candidates[i]);
                }
            }
            result.add(subResult);
            return;
        }
        if (startIndex >= candidates.length) {
            return;
        }
        int num = 0;
        while (num <= target) {
            combinationSum(candidates, target - num, result, tmp, startIndex + 1);
            num += candidates[startIndex];
            tmp[startIndex]++;
        }
        tmp[startIndex] = 0;
    }
}

class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] array = new int [2];

        int i = 0; 
        int j = 0;

        for(; i < nums.length; i++) {
            
            for (j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    array[0] = i;
                    array[1] = j;

                    return array;
                }
            }
        }

        return array;
    }
}

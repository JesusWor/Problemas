import java.util.Arrays;

public class RemoveDuplicatesFromSortedArray {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArray sol = new RemoveDuplicatesFromSortedArray();
        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int k = sol.removeDuplicates(nums);

        System.out.println("k: " + k);
        System.out.println("Array modificado: " + Arrays.toString(Arrays.copyOf(nums, k)));
    }
}
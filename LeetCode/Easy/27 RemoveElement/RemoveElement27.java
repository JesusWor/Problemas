import java.util.Arrays;

public class RemoveElement27 {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }

    public static void main(String[] args) {
        RemoveElement27 sol = new RemoveElement27();
        int[] nums = {0, 1, 2, 2, 3, 0, 4, 2};
        int val = 2;
        int k = sol.removeElement(nums, val);
        
        System.out.println("k: " + k);
        System.out.println("Array: " + Arrays.toString(Arrays.copyOf(nums, k)));
    }
}
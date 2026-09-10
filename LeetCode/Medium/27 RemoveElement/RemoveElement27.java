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

        int[] nums = {3, 2, 2, 3};
        int val = 3;

        int k = sol.removeElement(nums, val);

        System.out.println("Nueva longitud k: " + k);
        System.out.print("Arreglo modificado: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }
}
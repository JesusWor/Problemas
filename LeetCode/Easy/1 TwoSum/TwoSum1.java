import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;

public class TwoSum1 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complemento = target - nums[i];
            if (map.containsKey(complemento)) {
                return new int[]{map.get(complemento), i};
            }
            map.put(nums[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        TwoSum1 sol = new TwoSum1();
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] resultado = sol.twoSum(nums, target);
        System.out.println(Arrays.toString(resultado));
    }
}
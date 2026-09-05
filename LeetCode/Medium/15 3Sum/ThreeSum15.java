import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> resultados = new ArrayList<>();
        Arrays.sort(nums);
        int n = nums.length;

        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int j = i + 1;
            int k = n - 1;

            while (j < k) {
                int suma = nums[i] + nums[j] + nums[k];

                if (suma == 0) {
                    resultados.add(Arrays.asList(nums[i], nums[j], nums[k]));

                    while (j < k && nums[j] == nums[j + 1]) j++;
                    while (j < k && nums[k] == nums[k - 1]) k--;

                    j++;
                    k--;
                } else if (suma < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        return resultados;
    }

    public static void main(String[] args) {
        ThreeSum15 sol = new ThreeSum15();
        int[] nums = {-1, 0, 1, 2, -1, -4};
        List<List<Integer>> resultado = sol.threeSum(nums);
        System.out.println(resultado);
    }
}
public class ContainerWithMostWater11 {
    public int maxArea(int[] height) {
        int l = 0;
        int r = height.length - 1;
        int ans = 0;
        while (l < r) {
            int ancho = r - l;
            int alto = Math.min(height[r], height[l]);
            int area = ancho * alto;
            ans = Math.max(ans, area);
            if (height[l] < height[r]) {
                l++;
            } else {
                r--;
            }
        }
        return ans;
    }

    public static void main(String[] args) {
        ContainerWithMostWater11 sol = new ContainerWithMostWater11();
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        int resultado = sol.maxArea(height);
        System.out.println(resultado);
    }
}
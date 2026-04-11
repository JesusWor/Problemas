package HackeRanck.Arrays;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;
import java.util.List;

class Result {

    /*
     * Complete the 'getTotalX' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     * 1. INTEGER_ARRAY a
     * 2. INTEGER_ARRAY b
     */

    public static int getTotalX(List<Integer> a, List<Integer> b) {
        // Write your code here
        if (a == null || b == null || a.isEmpty() || b.isEmpty()) {
            return 0;
        }
        int maxA = a.stream().max(Integer::compareTo).orElse(Integer.MIN_VALUE);
        int minB = b.stream().min(Integer::compareTo).orElse(Integer.MAX_VALUE);
        int contador = 0;
        for (int i = maxA; i <= minB; i++) {
            boolean numeroValido = true;

            for (int numa : a) {
                if (i % numa != 0) {
                    numeroValido = false;
                    break;
                }
            }

            if (numeroValido) {
                for (int numb : b) {
                    if (numb % i != 0) {
                        numeroValido = false;
                        break;
                    }
                }
            }

            if (numeroValido) {
                contador++;
            }
        }
        return contador;
    }

}

public class BetweenTowSets {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] firstMultipleInput = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int n = Integer.parseInt(firstMultipleInput[0]);

        int m = Integer.parseInt(firstMultipleInput[1]);

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        List<Integer> brr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                .map(Integer::parseInt)
                .collect(toList());

        int total = Result.getTotalX(arr, brr);

        bufferedWriter.write(String.valueOf(total));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}

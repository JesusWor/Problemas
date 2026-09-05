public class ZigzagConversion6 {
    public static String convert(String s, int numRows) {
        int separation;
        String exit = "";
        char[] arreglo = s.toCharArray();
        if(numRows==1){
            return s;
        }
        else{
            separation = numRows - 2;
            for(int i=0; i<numRows; i++){
                for(int j=i; j<arreglo.length; ){
                    exit += arreglo[j];
                    if(i==0 || i==numRows-1){
                        j += (2*separation + 2);
                    }
                    else{
                        j += (2*separation + 2);
                        if(j - (2*i) < arreglo.length){
                            exit += arreglo[j - (2*i)];
                        }
                    }
                }
            }    
        }
        return exit;
    }
    
    public static void main(String[] args) {
        System.out.println(convert("PAYPALISHIRING", 3));
    }
}

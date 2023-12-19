import java.util.Arrays;

class Sort {
    public static void main(String[] args) {
        Integer[] arra = {9,8,7,6,5,4,3,2,1};
        Arrays.sort(arra);
        for (int num : arra) {
            System.out.print(num + " ");
        }
        System.out.print("\n");
    }
}
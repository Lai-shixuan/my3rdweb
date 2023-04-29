// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public  static int cut4pieces(double x, double y){
       if (x == 0 || y == 0)
           return 0;
       else if (x > 0) {
           if (y > 0)
               return 1;
           else return 4;
       }else if (y > 0)
           return 2;
       else return 3;
    }
    public static void main(String[] args) {
        // Press Alt+Enter with your caret at the highlighted text to see how
        // IntelliJ IDEA suggests fixing it.
        double x = 24.3;
        double y = -22;
        System.out.println(cut4pieces(x, y));
    }
}
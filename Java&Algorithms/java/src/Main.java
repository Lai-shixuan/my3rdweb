import java.util.ArrayList;
import java.util.List;

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
        Dog abc = new Dog();
        Dog def = new Dog();
        def.size = 80;
        Dog bigger = abc.Sizemaxdog(def);
        System.out.println(abc);

        int[] arr1 = new int[10];
        arr1[0] = 1;
        arr1[1] = 2;
        System.out.println(arr1);

        Integer c1 = new Integer(10);
        System.out.println(c1);
    }

   public static class Dog{
        int size = 30;
        static int name = 40;

        public int Sizemax(){
            if (name > 20)
                return 10;
            return 20;
       }

       public Dog Sizemaxdog(Dog otherdog){
            if (size > otherdog.size)
                return this;
            return otherdog;
       }
   }

}
import org.checkerframework.checker.units.qual.A;

import java.util.ArrayList;
import java.util.List;

public class ListExercises {

    /** Returns the total sum in a list of integers */
	public static int sum(List<Integer> L) {
        int len = L.size();
        int sum = 0;
        for (int i : L) {       // don't know what may happen if i > L = 0;
            sum = sum + i;
        }
        return sum;
    }

    /** Returns a list containing the even numbers of the given list */
    public static List<Integer> evens(List<Integer> L) {
        List<Integer> newlist = new ArrayList<>();
        for (int i : L){
            if (i % 2 == 0){
                newlist.add(i);
            }
        }
        return newlist;
    }

    /** Returns a list containing the common item of the two given lists */
    public static List<Integer> common(List<Integer> L1, List<Integer> L2) {
        List<Integer> listcommon = new ArrayList<>();
        for (int i : L1){
            if (L2.contains(i))
                listcommon.add(i);
        }
        return listcommon;
    }


    /** Returns the number of occurrences of the given character in a list of strings. */
    public static int countOccurrencesOfC(List<String> words, char c) {
        String all = words.toString();
        int flag = 0;
        for (int i = 0; i < all.length(); i++){
            if (c == all.charAt(i))
                flag++;
        }
        return flag;
    }

}

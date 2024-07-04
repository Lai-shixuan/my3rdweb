/* *****************************************************************************
 *  Name:              Ada Lovelace
 *  Coursera User ID:  123456
 *  Last modified:     October 16, 1842
 **************************************************************************** */

import edu.princeton.cs.algs4.StdIn;

public class RandomWord {
    public static void main(String[] args) {
        int wordsNumber = 0;
        String a = ""; // Initialize variable a
        String temp = "";

        while (!StdIn.isEmpty()) {
            double p = 1.0 / (wordsNumber + 1);
            temp = StdIn.readString();
            if (Math.random() < p) {
                a = temp;
            }
            wordsNumber++;
        }
        System.out.println(a);
    }
}
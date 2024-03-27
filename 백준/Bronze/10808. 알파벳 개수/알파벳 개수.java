import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
    // click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
    public class Main {

        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            ArrayList<Integer> aL = new ArrayList<>(Collections.nCopies(26,0));
            String s = br.readLine();
            for(int i=0; i < s.length(); i++){
                char c = s.charAt(i);
                int value = aL.get(c-97);
                aL.set(c - 97, value+1);
            }
            for(int i =0; i< 26; i++){
                System.out.print(aL.get(i)+" ");
            }
        }
    }
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String st = br.readLine().toUpperCase();
        HashMap<Character,Integer> h = new HashMap<>();

        int maxCount = 0;
        char maxChar = '?';

        for(int i =0; i< st.length(); i++){
            char currentChar = st.charAt(i);
            h.put(currentChar,h.getOrDefault(currentChar, 0)+1);
            if(h.get(currentChar) > maxCount){
                maxCount = h.get(currentChar);
                maxChar = currentChar;
            }
        }
        int countMax = 0;
        for(char key : h.keySet()){
            if(h.get(key)==maxCount){
                countMax++;
                if(countMax > 1){
                    maxChar = '?';
                    break;
                }
            }
        }
        System.out.println(maxChar);
    }
}


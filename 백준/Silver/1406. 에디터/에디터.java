import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
    // click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
    public class Main {

        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
            String input = br.readLine();
            int M = Integer.parseInt(br.readLine());

            Stack<Character> org = new Stack<>();
            Stack<Character> tmp = new Stack<>();
            int len = input.length();
            for (int i = 0; i < len; i++) org.add(input.charAt(i));
            for(int i = 0;i<M;i++){
                String cmdStr = br.readLine().replace(" ","");
                char[] cmd = cmdStr.toCharArray();

                switch (cmd[0]){
                    case 'P':
                        org.add(cmd[1]);
                        break;
                    case 'L':
                        if(!org.isEmpty()) tmp.add(org.pop());
                        break;
                    case 'D':
                        if(!tmp.isEmpty()) org.add(tmp.pop());
                        break;
                    case 'B':
                        if(!org.isEmpty()) org.pop();
                }
            }
            while(!tmp.isEmpty()) org.add(tmp.pop());
            for(Character ch : org) bw.write(ch);
            bw.close();
        }
    }
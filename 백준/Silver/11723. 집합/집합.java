import java.io.*;
import java.nio.Buffer;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        HashSet<Integer> set = new HashSet<>();

        // 횟수
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int x = 0;
            if(!command.equals("all") && !command.equals("empty")){
                x = Integer.parseInt(st.nextToken());
            }
            switch (command){
                case "add":
                    set.add(x);
                    break;
                case  "remove":
                    set.remove(x);
                    break;
                case "check":
                    if(set.contains(x)){
                        bw.write("1\n");
                    }else{
                        bw.write("0\n");
                    }
                    break;
                case "toggle":
                    if(set.contains(x)){
                        set.remove(x);
                    }else{
                        set.add(x);
                    }
                    break;
                case "all":
                    for (int j = 1; j <= 20; j++){
                        set.add(j);
                    }
                    break;
                case "empty":
                    set.clear();
            }
        }
        bw.flush();
        bw.close();
    }
}


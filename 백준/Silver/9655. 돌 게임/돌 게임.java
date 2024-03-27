import java.io.*;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int stone = Integer.parseInt(br.readLine());
        
        br.close();
        
        if( stone % 2 == 0){
            bw.write("CY");
        } else{
            bw.write("SK");
        }
     
        bw.flush();
        bw.close();
    }
}
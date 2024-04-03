import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Status {
    int weight;
    int height;

    public Status(int w, int h) {
        this.weight = w;
        this.height = h;
    }
    public boolean compareWith(Status o){
        // 양쪽이 다 클때 크다
        if(this.height>o.height && this.weight > o.weight){
            return true;
        } else{
            return false;
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        Status[] list = new Status[n];
        for(int i =0; i<n;i++){
            StringTokenizer a = new StringTokenizer(br.readLine());
            int w = Integer.parseInt(a.nextToken());
            int h = Integer.parseInt(a.nextToken());
            list[i] = new Status(w,h);
        }
        for(int i = 0;i<n;i++){
            int rank = 1;
            for(int j = 0; j<n;j++){
                if(list[j].compareWith(list[i]))
                    rank++;
            }
            System.out.print(rank+" ");
        }
    }
}
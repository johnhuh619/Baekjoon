    import java.io.BufferedReader;
    import java.io.IOException;
    import java.io.InputStreamReader;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    import java.util.StringTokenizer;

    // 자바는 객체 지향적으로 풀면 좋다고 들어서, 사용자 정의 클래스 Country를 만들어 접근해 보았다.
    // 사용자 정의 클래스를 만들려면 일단 Interface를 만들어야 해서 알아보았다.
    //
    class Country implements Comparable<Country> {
        int num;
        int gold;
        int silver;
        int bronze;

        public Country(int num, int gold, int silver, int bronze) {
            this.num = num;
            this.gold = gold;
            this.silver = silver;
            this.bronze = bronze;
        }

        // compareTo를 임의로 재정의
        @Override
        public int compareTo(Country other) {
            if (this.gold != other.gold) {
                return other.gold - this.gold;
            } else if (this.silver != other.silver) {
                return other.silver - this.silver;
            } else {
                return other.bronze -this.bronze;
            }
        }

    }


    public class Main {

        public static void main(String[] args) throws IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken()); // 국가 수
            int M = Integer.parseInt(st.nextToken()); // 등수 알고 싶은 국가

            List<Country> countries = new ArrayList<>();

            // 일단 떄려박기
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                int num = Integer.parseInt(st.nextToken());
                int gold = Integer.parseInt(st.nextToken());
                int silver = Integer.parseInt(st.nextToken());
                int bronze = Integer.parseInt(st.nextToken());
                countries.add(new Country(num, gold, silver, bronze));
            }
            Collections.sort(countries);

            //등수 계산
            int rank = 1;
            int sameRank = 1;
            Country prevCountry = countries.get(0);
            if (prevCountry.num == M){
                System.out.println(rank);
                return;
            }
            for(int i = 1; i<countries.size(); i++){
                Country currentCountry = countries.get(i);
                if (!currentCountry.equals(countries.get(i-1))){
                    rank+= sameRank;
                    sameRank = 1;
                }else {
                    sameRank++;
                }
                if(currentCountry.num == M){
                    System.out.println(rank);
                    return;
                }
            }
        }
    }


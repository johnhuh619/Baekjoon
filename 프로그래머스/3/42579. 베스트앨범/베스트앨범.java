import java.util.*;

class Album implements Comparable<Album> {
    String genre;
    int play;
    int idx;
    
    Album(String genre, int play, int idx) {
        this.genre = genre;
        this.play = play;
        this.idx = idx;
    }
    
    @Override
    public int compareTo(Album other) {
        if(this.play == other.play) {
             return Integer.compare(this.idx, other.idx);
        }
        return Integer.compare(other.play,this.play);
    }
}

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        
        Map<String, Integer> genSum = new HashMap<>();
        List<Album> albums = new ArrayList();
        
        for (int i =0; i < genres.length; i++ ){
            genSum.put(genres[i], genSum.getOrDefault(genres[i],0) + plays[i]);
            albums.add(new Album(genres[i], plays[i], i));
        }
        
        List<Map.Entry<String, Integer>> genreOrder = new ArrayList<>(genSum.entrySet());
        genreOrder.sort((a,b) -> b.getValue() - a.getValue());
        
        Collections.sort(albums);
        
        List<Integer> answer = new ArrayList<>();
        
        for (Map.Entry<String, Integer> entry: genreOrder){
            String g = entry.getKey();
            int cnt = 0;
            
            for(Album a: albums){
                if(a.genre.equals(g)){
                    answer.add(a.idx);
                    cnt++;
                }
                if(cnt == 2) break;
            }
        }                      
        return answer.stream().mapToInt(i->i).toArray();
    }
}
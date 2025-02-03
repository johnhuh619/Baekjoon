import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = new HashMap();
        
        for(String p_num: phone_book){
            map.put(p_num,map.getOrDefault(p_num,0));
        }
        
        for(String s: phone_book){
            for(int j=0; j<s.length(); j++){
                if(map.containsKey(s.substring(0,j))) return false;
            }
        }
        
        return true;
    }
}


// prefix 를 구한다
// 문자열 슬라이싱 -> substring 

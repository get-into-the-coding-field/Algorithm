package 윤.w11;

import java.util.HashMap;
import java.util.Map;

public class Login {
    public static void main(String[] args) throws Exception {
        Solution solution = new Solution();
        String[] id_pw = {"meosseugi", "1234"};
        String[][] db = {{"rardss", "123"}, {"yyoom", "1234"}, {"meosseugi", "1234"}};
        System.out.println("======================================");
        System.out.println("my answer : " + solution.solution(id_pw, db)); // "login"
        System.out.println("======================================");
    }
}

class Solution {
    public String solution(String[] id_pw, String[][] db) {
        Map<String, String> users = new HashMap<>();

        for (String[] info : db) {
            users.put(info[0], info[1]);
        }

        return users.containsKey(id_pw[0]) ? (users.get(id_pw[0]).equals(id_pw[1]) ? "login" : "wrong pw") : "fail";

    }
}
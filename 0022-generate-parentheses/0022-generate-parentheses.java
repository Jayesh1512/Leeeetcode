class Solution {
    public List<String> generateParenthesis(int n) {
        String ans = "";
        ArrayList<String> result = new ArrayList<String>();
        generate(n,result,ans,0,0);
        return result;
    }
    public static void generate(int n, ArrayList<String> result , String ans , int open, int closed){
        if(open == closed && open == n){
            result.add(ans);
        }
        if(open < n){
            generate(n,result,ans+'(',open+1,closed);
        }
        if(open > closed){
            generate(n,result,ans+')',open,closed+1);
        }
    }
}
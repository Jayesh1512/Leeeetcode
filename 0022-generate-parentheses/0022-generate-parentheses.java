class Solution {
    public List<String> generateParenthesis(int n) {
        int open = n;
        int closed = n;
        ArrayList<String> a = new ArrayList<String>();
        birthday(open,closed,"",a);
        return a;
    }

    public void birthday(int open,int closed,String s , ArrayList<String>res){
        if(open == closed && open == 0){
            res.add(s);
            return;
        }
        if (open > 0) {
            birthday(open-1, closed, s + "(", res);
        }

        if (closed > open) {
            birthday(open, closed - 1, s + ")",  res);
        }
    }
}
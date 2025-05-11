class Solution {
    public boolean wordPattern(String pattern, String s) {
        Map<Character, String> map = new HashMap<>();
        Set<String> setOfWords = new HashSet<>();
        String[] words = s.split(" ");
        if (pattern.length() != words.length) return false;
        for (int i = 0; i < words.length; i++) {
            if (map.containsKey(pattern.charAt(i))) {
                if (!words[i].equals(map.get(pattern.charAt(i)))) return false;
            } else {
                if (setOfWords.contains(words[i])) return false;
                map.put(pattern.charAt(i), words[i]);
                setOfWords.add(words[i]);
            }
        }
        return true;
    }
}
class Solution {
    private static void addWord(Map<String , List<String>> map, String pattern, String word){
        map.computeIfAbsent(pattern, k -> new ArrayList<>()).add(word);
    }
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        boolean exists = false;
        for (String word : wordList) if (word.equals(endWord)) exists = true;
        if (!exists) return 0;

        Map<String, List<String>> patternMap = new HashMap<>();
        for (String c : wordList){
            for (int j=0; j<c.length(); j++){
                String pattern = c.substring(0,j) +"*"+ c.substring(j+1);
                addWord(patternMap, pattern, c);
            }
        }

        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        Set<String> visited = new HashSet<>();
        visited.add(beginWord);
        int level = 1;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String currentWord = queue.poll();
                if (currentWord.equals(endWord)) return level;

                for (int j = 0; j < currentWord.length(); j++) {
                    String pattern = currentWord.substring(0, j) + "*" + currentWord.substring(j + 1);
                    List<String> neighbors = patternMap.getOrDefault(pattern, new ArrayList<>());
                    for (String neighbor : neighbors) {
                        if (!visited.contains(neighbor)) {
                            visited.add(neighbor);
                            queue.add(neighbor);
                        }
                    }
                }
            }
            level++;
        }
        return 0;
    }
}
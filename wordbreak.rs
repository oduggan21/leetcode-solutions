impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        use std::collections::HashSet;

        let word_set: HashSet<&str> = word_dict.iter().map(|w| w.as_str()).collect();
        let length = s.len();
        let mut values = vec![false;length+1];
        values[0] = true;


        for i in 1..length+1{
            for j in 0..i{
                if values[j] && word_set.contains(&s[j..i]){
                    values[i] = true;
                }
            }
        }
        return values[length]
    }
}

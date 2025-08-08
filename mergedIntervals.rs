impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        if intervals.is_empty(){
            return vec![];
        }
        let mut intervals = intervals; // now it's mutable
    intervals.sort_by_key(|v| v[0]);
    let mut res: Vec<Vec<i32>> = vec![];
    let (mut currL, mut currR) = (intervals[0][0], intervals[0][1]);

    for interval in &intervals[1..] {
        let L = interval[0];
        let R = interval[1];
        if L <= currR{
            currR = std::cmp::max(currR, R);
        }
        else{
            res.push(vec![currL,currR]);
            currL = L; currR = R;
        }
    }
    res.push(vec![currL, currR]);
    res
    }
}

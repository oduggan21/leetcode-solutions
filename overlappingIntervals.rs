impl Solution {
    pub fn erase_overlap_intervals(intervals: Vec<Vec<i32>>) -> i32 {
        let mut intervals = intervals;
        intervals.sort_by_key(|x| x[1]);
        let mut count: i32 = 0;
        let mut prevHigh = intervals[0][1];

        let n = intervals.len();

        for i in 1..n {
            if intervals[i][0] < prevHigh{
                count += 1;
            }
            else{
                prevHigh = intervals[i][1];
            }
        }
        count
    }
}

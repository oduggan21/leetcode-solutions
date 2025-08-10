function eraseOverlapIntervals(intervals: number[][]): number {
    if (intervals.length <= 0){
        return 0;
    }
    intervals.sort((a,b) => a[1]-b[1]);

    let count = 0;
    let prev = intervals[0][1];

    for(let i = 1; i < intervals.length; i++){
        if (intervals[i][0] < prev){
            count++;
        }
        else{
            prev = intervals[i][1]
        }
    }
    return count;
};

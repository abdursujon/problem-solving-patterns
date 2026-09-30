'''
The Merge Intervals pattern is a powerful technique used to deal with overlapping intervals or ranges. 
It involves sorting and then merging intervals based on specific conditions. This pattern is incredibly 
useful for time-based problems, scheduling, and range manipulation.

Usage
    • Overlapping Intervals: Perfect for problems where you need to merge overlapping intervals or find if an interval overlaps with any other.
    • Interval Scheduling: Useful for problems that involve scheduling based on time intervals.

Pros and Cons
    • Pros:
        ◦ Clarity: Provides a clear and systematic way to deal with overlapping intervals.
        ◦ Efficiency: Helps in reducing the problem complexity and achieving optimal solutions.
    • Cons:
        ◦ Sorting Overhead: Requires the intervals to be sorted beforehand, which could add to the time complexity.
        ◦ Specificity: Mainly beneficial for problems involving intervals and ranges.

Example Problems from Grokking the Coding Interview
    1. Merge Intervals: Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.
    2. Insert Interval: Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.
    3. Intervals Intersection: Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
'''


# Three steps: 
# Step 1: Sort by start time 
# Step 2: Create a merge list and two variable for start and end 
# Step 3: For each loop to track overlapping 
def merge(intervals):
    if len(intervals) < 2:
        return intervals

    # sort the intervals list with starting time so we can merge them 
    intervals.sort(key=lambda x: x[0]) # key is the rule what to sort by. The rule is the lambda function here lambda x: x[0] means use items first number and sort them in acending order 

    # create a new list to add merge intervals 
    merged_intervals = []
    start = intervals[0][0] # first inner list interval, then it's first element 
    end = intervals[0][1] # first inner list interval, then it's second element

    for i in range(1, len(intervals)):
        # i is each interval from the intervals list 
        interval = intervals[i] # each inner list (interval)
        if interval[0] <= end: # overlapping 
            end = max(interval[1], end) # check if first interval and current interval end is overlapping and choose which one has higher end value 
        else: # none overlapping interval, add the previous interval and reset 
            merged_intervals.append([start, end])
            start = interval[0]
            end = interval[1]

    # add the last interval 
    merged_intervals.append([start, end])
    return merged_intervals

print(merge([[2, 5], [3, 4], [8, 9]]))


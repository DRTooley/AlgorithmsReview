# In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted
# sum of completion times..
#
# Download the text file below.
# jobs.txt
#
# This file describes a set of jobs with positive and integral weights and lengths. It has the format
#
# [number_of_jobs]
#
# [job_1_weight] [job_1_length]
#
# [job_2_weight] [job_2_length]
#
# ...
#
# For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.
#
# You should NOT assume that edge weights or lengths are distinct.
#
# Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference
# (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal
# difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a
# different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the
# resulting schedule --- a positive integer --- in the box below.
#
# ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases
# to the discussion forum).
#
#
# 2.
#
# For this problem, use the same data set as in the previous problem.
#
# Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio
# (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted
# completion times of the resulting schedule --- a positive integer --- in the box below.

class Task:
    def __init__(self, weight, length):
        self.length = int(length)
        self.weight = int(weight)

    def cost(self):
        return self.weight - self.length

    def __lt__(self, other):
        c = self.cost()
        oc = other.cost()

        if c == oc:
            return self.weight < other.weight
        else:
            return c < oc



    def __gt__(self, other):
        return not self.__lt__(other)

    def __repr__(self):
        return 'Cost: {}   Weight: {}\n'.format(self.cost(), self.weight)

class RatioTask(Task):
    def __int__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)

    def cost(self):
        return self.weight/self.length

def ReadTasks(file_name):
    tasks = []
    ratio_tasks = []
    with open(file_name, 'r') as task_file:
        task_count = task_file.readline()
        for line in task_file:
            line_split = line.split()
            tasks.append(Task(line_split[0], line_split[1]))
            ratio_tasks.append(RatioTask(line_split[0], line_split[1]))
    return tasks, ratio_tasks

def ComputeWeightedCompletionTimes(tasks):
    completion_time = 0
    sum = 0
    for t in tasks:
        completion_time += t.length
        sum += completion_time * t.weight
        #print(completion_time)
    print('Sum: {}'.format(sum))


if __name__ == '__main__':
    tasks, ratio_tasks = ReadTasks('jobs.txt')
    decreasing_order_tasks = sorted(tasks, reverse=True)
    decreasing_order_ratio_tasks = sorted(ratio_tasks, reverse=True)
    #print(decreasing_order_tasks)
    ComputeWeightedCompletionTimes(decreasing_order_tasks)
    ComputeWeightedCompletionTimes(decreasing_order_ratio_tasks)
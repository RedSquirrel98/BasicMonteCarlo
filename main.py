
#
# Very basic Monte Carlo Simulator for ENGR 303
#
import numpy
import math
from math import sqrt 
import random
import matplotlib.pyplot as plt


class activity:
    def __init__(self, name, minduration,maxduration):
        self.ID=name
        self.min=minduration
        self.max= maxduration

#this function generates a random number between an interval
def random_number(minvalue, maxvalue):
    range= maxvalue-minvalue
    result=random.uniform(0,1)
    return minvalue+range*result

# this function calculates the average duration of the CP (using randomly generated durations) for each iteration  
def avg_duration_calc(CP_List, iterations):
    avg_duration=[]
    for i in range(iterations):
        rand_list=[]
        for obj in CP_List:
            rand= random_number(obj.min, obj.max)
            rand_list.append(rand)
        avg_duration.append(sum(rand_list)) 
    return avg_duration

# this function calculates the average duration time of all the iterations 
def mean_duration_calc(avg_duration, iterations):
    mean_duration=sum(avg_duration)/iterations
    return mean_duration

#this function calculates the standard deviation of all iterations 
def STD_calc(mean_duration, avg_duration, iterations):
    variance=0
    for i in range(iterations):
        variance=variance+ (avg_duration[i]-mean_duration)**2
    variance= variance/iterations 
    STD=sqrt(variance)
    print('Mean: {} -- Variance: {} -- Standard Deviation: {}'.format(mean_duration, variance, STD))


#this function uses matplotlib to plot the CDF of the mean path time 
def plot_CDF(avg_duration, iterations):
    confidence =[]
    avg_sort=sorted(avg_duration)                             # this will be our y axis 
    confidence=numpy.arange(0, 100, 100/iterations).tolist()  # this will be our x axis 
    plt.plot(avg_sort,confidence)
    plt.xlabel("Duration")
    plt.xticks(numpy.arange(numpy.round(avg_sort[0]), numpy.round(avg_sort[-1]), step=1))   
    plt.ylabel("Confidence")
    plt.yticks(numpy.arange(0, 100,step=10))
    plt.title("Critical Path CDF")
    plt.grid(b=True, which='major', axis='both')
    plt.show()
# this function uses matplotlib to plot the PDF of the mean path time   
def plot_PMF(avg_duration, iterations):
    avg_rounded= numpy.round(avg_duration)   
    min_bound=int(numpy.amin(avg_rounded))
    print(type(min_bound))
    max_bound=int(numpy.amax(avg_rounded))
    occurence_array=[]

    def find_occurences(value_given):
        occurrences=0
        occurrences = numpy.count_nonzero(avg_rounded == value_given)
        return occurrences

    for i in range(min_bound,max_bound+1,1):
        occurence_array.append(find_occurences(i))  
    # print(sorted(avg_rounded))
    # print(occurence_array)
    xlab=numpy.arange(min_bound, max_bound+1, 1).tolist()
    plt.bar(xlab,occurence_array)
    plt.ylabel("Number of Occurences for Given CP Length")
    plt.xlabel("Calculated CP Length")
    plt.title("Critical Path PMF")
    plt.grid(b=True, which='major', axis='both')
    plt.show()
    

def main():

    #list of activities on the critical path: find a way to enter these into a GUI for later
    A= activity("A",8,9)   
    B= activity("B",10,12)   
    C= activity("C",18,22)   
    D= activity("D",10,15)   
    E= activity("E",10,12)  
    CP_List= [A,B,C,D,E] 
    iterations = 10000  # specify number of Monte Carlo Iterations
    
    avg_duration = avg_duration_calc(CP_List,iterations)
    mean_duration = mean_duration_calc(avg_duration,iterations)
    STD_calc(mean_duration, avg_duration, iterations)
    plot_CDF(avg_duration, iterations)
    plot_PMF(avg_duration, iterations)


if __name__ == "__main__":
	main()      





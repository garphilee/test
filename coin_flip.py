import random
#import matplotlib
    # issue with m1 mac not working with matplotlib, numpy, pip, etc
    ## https://apple.stackexchange.com/questions/421486/m1-mac-mini-python-reports-mach-o-but-wrong-architecture

def flip():
    global coin
    #flip coin
    flip_coin = random.randint(0,1)
    if flip_coin == 0:
        coin = "Tails"
    else:
        coin = "Heads"
    return coin

"""
1. flip coin
2. if heads, keep flipping until tails.
3. record number of consecutive Heads, save - ie. this run had 1 Head, next run had 2, etc...
4. Reset head + tail head count
5. keep tally of all consecutive runs of heads - "there were 5 runs that had only 1 consecutive head, 3 runs with 2 consecutive heads, etc..."
"""

def consec_heads(runs):
    #go through specified number of times (runs)
    #tail_count = 0
    head_count = 0
    total_head_count = 0
    record = []
    #for graphing purposes
    numbers = []
    lables = []
    unique_list = []
    total_runs = runs
    while runs > 0:
        flip()
        if coin == "Heads":
            # test print
            #print("flipped heads")
            head_count += 1
            total_head_count += 1
        else:
            # test print
            #print("flipped tails")
            #print("You flipped " + str(head_count) + " consecutive Heads!")

            record.append(head_count)
            head_count = 0
            #tail_count += 1
            runs -= 1
    print("You are done flipping.")
    print("------------------")
    print("Statistics: ")
    # if number of runs is high, don't display record because it'd be too much
    if total_runs <= 100:
        print("Record of flips: " + str(record))
    print("Max consecutive Head streak: " + str(max(record)))
    print("Average streak: " +str((sum(record)/len(record))))
    #total number of heads versus tails
    print("Total number of Heads flipped: " +str(total_head_count))
    # finding max streak
    print("Max streak is: " + str(max(record)))

    #create list of unique numbers, then FOR (loop) each of those elements, count how many occured in the record of flips
    ##create list of unique numbers/ or just max(list) and n-1 until 0 to go through all possible streaks

    for i in range(max(record)):
        unique_list.append(i+1)

    """ # test for below
    print("List of unique elements: " + str(unique_list))
    """

    # lists count for unique items
    ## want to round percentage place based on the total_runs (original runs) to give nice legible percentages
    for i in unique_list:
        print(str(i) + " count: " + str(record.count(i)) + "(" + str(round(record.count(i)/total_runs*100, len(str(total_runs)))) + "%)")


    #print(str(unique_list(i)) + " count: " + str(unique_list.count(record,i)))

    # find occurances of each item(unique streak) in list
    ## starting with highest streak, count how many times that streak has occured

"""
    # finding max streak
    list_count = max(record)


    #print("List Count is: " + str(list_count))
    # from highest streak, go down by 1 streak until zero, count number of occurences.
    while list_count >= 0:
        print("'" + str(list_count) + "'" + " occured " + str(record.count(list_count)) + " many times.")

        numbers.append(record.count(list_count))
        labels.append(list_count)
        print(numbers)
        print(labels)

        list_count -= 1
"""
"""
    # ------------------------ #
    # matplotlib
    ## bar chart of occurances
    def bar_chart(numbers,labels,pos):
        plt.bar(pos,numbers,color='blue')
        plt.xticks(ticks=pos,labels=labels)
        plt.show()
"""
consec_heads(10000000)

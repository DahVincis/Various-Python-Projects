# define a function that performs quick sort
def quickSort(alist):
    # call the helper function to perform the sorting on the whole list
    quickSortHelper(alist,0,len(alist)-1)

# define a helper function that performs the quick sort
def quickSortHelper(alist,first,last):
    # check if there are more than 1 elements in the list
    if first < last:
        # partition the list and get the split point
        splitpoint = partition(alist,first,last)
        # recursively call the helper function to sort the left sublist
        quickSortHelper(alist,first,splitpoint-1)
        # recursively call the helper function to sort the right sublist
        quickSortHelper(alist,splitpoint+1,last)

# define a function that partitions the list
def partition(alist,first,last):
    # select the first element as the pivot value
    pivotvalue = alist[first]
    # initialize the left and right markers
    leftmark = first+1
    rightmark = last
    done = False
    # loop until the markers cross each other
    while not done:
        # move the left marker to the right until it finds an element greater than the pivot value
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # move the right marker to the left until it finds an element less than the pivot value
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        # check if the markers have crossed each other
        if rightmark < leftmark:
            done = True
        else:
            # swap the elements at the left and right markers
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    # swap the pivot value with the element at the right marker
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    # return the right marker as the split point
    return rightmark

# create a list of integers to be sorted
alist = [93645, 4768, 259643, 8517, 41637, 98421, 1843, 74926, 30451, 52406, 9637, 417, 67208, 2759, 50692, 3954, 70459, 1948, 89125, 1574, 67025, 90138, 389, 72165, 1309, 53972, 
         8735, 45869, 716, 27081, 6283, 94367, 5790, 24856, 65103, 3469, 91308, 3827, 90615, 149, 83496, 5016, 1268, 805, 41536, 95824, 298, 7351, 20973, 86104, 34652, 40758, 682, 
         930, 3654, 1850, 6581, 2109, 52741, 7015, 2495, 602, 7496, 305, 1902, 8245, 503, 4196, 98352, 1870, 974, 526, 932, 83175, 4759, 65287, 317, 98146, 5713, 46925, 801, 710, 
         9837, 60849, 9512, 1869, 30879, 529, 47650, 245, 96385, 857, 217, 43179, 6021, 579, 3294, 5203, 14806, 2304]
quickSort(alist)
# print the list
print(alist)
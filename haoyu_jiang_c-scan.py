import sys
# open system files
f = open(sys.argv[1], 'r')
# set start_point
start_point = int(f.readline())
# set input_request list
input_request = map(int, f.readline().split(','))
f.close()

def cscan_schedule(request_list,start_point):
    output_request = []
    more_start=[]
    less_start=[]
    equal_start=[]
    cost=[]

# check the request_list
    for request in request_list:
        if request < 0 or request > 199:
            print "the request_list is wrong"

# divide and sort groups in input_list
    for request in request_list:
        more_start = [request for request in request_list if request > start_point]
        less_start = [request for request in request_list if request < start_point]
        equal_start = [request for request in request_list if request == start_point]
    more_start.sort()
    less_start.sort()

# combine into output list
    for request in equal_start:
        output_request.append(request)
    for request in more_start:
        output_request.append(request)
    for request in less_start:
        output_request.append(request)
    print ','.join(map(str, output_request))

# caculate the cost
    if len(more_start)==0 and len(less_start)!=0:
        cost = (199 - start_point) + 199 + less_start[len(less_start) - 1]
    elif len(more_start)!=0 and len(less_start)==0:
        cost = (199 - start_point) + 199
    elif len(more_start) != 0 and len(less_start) != 0:
        cost = (199-start_point) + 199 + less_start[len(less_start)-1]
    elif len(more_start) == 0 and len(less_start) == 0:
        cost = 0
    print cost

cscan_schedule(input_request,start_point)


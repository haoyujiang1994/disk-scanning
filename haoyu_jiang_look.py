import sys
# open system files
f = open(sys.argv[1], 'r')
# set start_point
start_point = int(f.readline())
# set input_request list
input_request = map(int, f.readline().split(','))
f.close()

def look_schedule(request_list,start_point):
    output_request = []
    more_start=[]
    less_start=[]
    equal_start = []
    cost=[]

# check the request_list
    for request in request_list:
        if request < 0 or request > 199:
            print "the request_list is wrong"

# divide and sort groups in input_list
    more_start = [request for request in request_list if request > start_point]
    less_start = [request for request in request_list if request < start_point]
    equal_start = [request for request in request_list if request == start_point]
    more_start.sort()
    less_start.sort(reverse=True)

    for request in equal_start:
        output_request.append(request)

# decide the starting direction , combine into output_list , calculate the cost
    if len(more_start) == 0 and len(less_start) == 0:
        print ','.join(map(str, output_request))
        cost = 0
        print cost

    elif len(more_start)==0 and len(less_start)!=0:
        for request in less_start:
            output_request.append(request)
        print ','.join(map(str, output_request))
        cost = start_point - less_start[len(less_start)-1]
        print cost

    elif len(more_start)!=0 and len(less_start)==0:
        for request in more_start:
            output_request.append(request)
        print ','.join(map(str, output_request))
        cost = more_start[len(more_start)-1] - start_point
        print cost

    elif len(more_start) != 0 and len(less_start) != 0:
        if (more_start[0]-start_point) > (start_point-less_start[0]):
            for request in less_start:
                output_request.append(request)
            for request in more_start:
                output_request.append(request)
            print ','.join(map(str, output_request))
            cost = (start_point - less_start[len(less_start)-1]) + (more_start[len(more_start)-1] - less_start[len(less_start)-1])
            print cost

        elif (more_start[0]-start_point) < (start_point-less_start[0]):
            for request in more_start:
                output_request.append(request)
            for request in less_start:
                output_request.append(request)
            print ','.join(map(str, output_request))
            cost = (more_start[len(more_start)-1] - start_point) + (more_start[len(more_start)-1] - less_start[len(less_start)-1])
            print cost

        else:
            if start_point <= 99:
                for request in less_start:
                    output_request.append(request)
                for request in more_start:
                    output_request.append(request)
                print ','.join(map(str, output_request))
                cost = (start_point - less_start[len(less_start) - 1]) + (
                more_start[len(more_start) - 1] - less_start[len(less_start) - 1])
                print cost

            if start_point >= 100:
                for request in more_start:
                    output_request.append(request)
                for request in less_start:
                    output_request.append(request)
                print ','.join(map(str, output_request))
                cost = (more_start[len(more_start) - 1] - start_point) + (more_start[len(more_start) - 1] - less_start[len(less_start) - 1])
                print cost

look_schedule(input_request,start_point)


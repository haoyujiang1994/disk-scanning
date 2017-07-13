import sys
# open system files
# f = open(sys.argv[1], 'r')
# set start_point
# start_point = int(f.readline())
start_point = 100
old_start_point = start_point
# set input_request list
# input_request = map(int, f.readline().split(','))
input_request = [80,80,120,120,10,10,199,1,15,67]
# f.close()

def sstf_schedule(request_list, start_point):
    output_request = []
    ooutput_request = []
    more_start = []
    less_start = []
    equal_start = []
    cost = 0
# check the request_list
    for request in request_list:
        if request < 0 or request > 199:
            print "the request_list is wrong"
# loop to find the closest point
    while len(request_list) > 0:
        more_start = [request for request in request_list if request > start_point]
        less_start = [request for request in request_list if request < start_point]
        equal_start = [request for request in request_list if request == start_point]
        more_start.sort()
        less_start.sort(reverse=True)

        for request in equal_start:
            output_request.append(request)
            request_list.remove(request)

        if len(more_start) == 0 and len(less_start) != 0:
            for request in less_start:
                output_request.append(request)
                request_list.remove(request)

        elif len(more_start) != 0 and len(less_start) == 0:
            for request in more_start:
                output_request.append(request)
                request_list.remove(request)

        elif len(more_start) != 0 and len(less_start) != 0:
            if (more_start[0] - start_point) > (start_point - less_start[0]):
                 output_request.append(less_start[0])
                 start_point = less_start[0]
                 request_list.remove(less_start[0])

            elif (more_start[0] - start_point) < (start_point - less_start[0]):
                output_request.append(more_start[0])
                start_point = more_start[0]
                request_list.remove(more_start[0])

            else:

                if start_point == old_start_point:
                    if start_point <= 99:
                        output_request.append(less_start[0])
                        request_list.remove(less_start[0])
                    if start_point >= 100:
                        output_request.append(more_start[0])
                        request_list.remove(more_start[0])

                if start_point != old_start_point:
                    for request in output_request:
                         ooutput_request.append(request)
                    if len(output_request) ==1:
                        if start_point - old_start_point > 0:
                            output_request.append(more_start[0])
                            request_list.remove(more_start[0])
                        if start_point - old_start_point < 0:
                            output_request.append(less_start[0])
                            request_list.remove(less_start[0])

                    if len(ooutput_request) > 1:
                        if start_point - output_request[-2] == 0:# ==
                            if output_request[-2] - old_start_point > 0:
                                output_request.append(more_start[0])
                                request_list.remove(more_start[0])
                            if output_request[-2] - old_start_point < 0:
                                output_request.append(less_start[0])
                                request_list.remove(less_start[0])
                        if start_point - output_request[-2] > 0:
                            output_request.append(more_start[0])
                            request_list.remove(more_start[0])
                        if start_point - output_request[-2] < 0:
                            output_request.append(less_start[0])
                            request_list.remove(less_start[0])
                start_point = output_request[-1]


    print ','.join(map(str, output_request))
    cost = abs(output_request[0] - old_start_point)
    for i in range(0,len(output_request)-1):
        cost = cost + abs(output_request[i+1]-output_request[i])
    print cost

sstf_schedule(input_request, start_point)


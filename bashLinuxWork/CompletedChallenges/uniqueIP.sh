#!/usr/bin/env bash
#ip_list file looks like this
#88.249.123.246 GET 200
#204.14.121.43 GET 200
#49.11.110.6 GET 200

#In this directory you have a file with list of IP addresses called ip_list. Using the file, determine which IP address is the most recurring (listed the most times).


sort ip_list | cut -d' ' -f1 | uniq -c | sort -n | tail -1
#sort the contents of the file --> ascending
#pull out just the ip address. use cut with ' ' as the delimiter
#split out each unique instance, make a of how many of the same unique one there are
#sort based on the count 
#print out the last item on the sorted list (the ip with most uses)
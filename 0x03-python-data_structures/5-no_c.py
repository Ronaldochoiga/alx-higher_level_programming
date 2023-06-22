#!/usr/bin/python3



def no_c(my_string):

    cop = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(cop))

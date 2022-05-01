#!/usr/bin/env python3
#author: s arbogast
#creat bits for query and ack, encode with PIE, add string of 1s for CW
#write to file, this file can then be read by gnuradio file sink

import numpy as np

#queur header input, this is a limited list for a specific query
q_comand = np.array('i',[1,0,0,0])
q_DR = 0
q_M = np.array('i',[0,0])
q_TRext = 0
q_select = np.array('i',[0,0])
q_target = 0
q_Q = np.array('i',[0,0,0,0])
q_crc5 = np.array('i',[,,,,])

ack_comand = np.array('i',[0,1])
ack_RC16 = 

#build header
q_header = np.append(q_command,q_Dr,q_M,q_TRext,q_select,q_target,q_Q,q_crc5)
ack_header = np.append(ack_command,ack_RC16)

#encode the with PIE


def pie_encode(header)
    coded_header = np.array([])
    zero = np.array([1,0])
    one = np.array([1,1,1,0])    
    
    for x in header;
        if x == 0:
            np.append(coded_header,zero)
        else
            np.append(coded_header, one)
    
    return coded_header
    

#add string of ones for continuouse wave, this lets the tag respond
cw = np.ones(1000)
np.append(coded_header,cw)


#write to file, gnuradio will read from this file

if__name__=="__main__":
    
    main(wave)
    

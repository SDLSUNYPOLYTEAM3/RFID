#!/usr/bin/env python3
#author: s arbogast
#creat bits for query and ack, encode with PIE, add string of 1s for CW
#write to file, this file can then be read by gnuradio file sink

import numpy as np

#queur header input, this is a limited list for a specific query
q_command = np.array([1,0,0,0])
q_DR = 0
q_M = np.array([0,0])
q_TRext = 0
q_select = np.array([0,0])
q_target = 0
q_Q = np.array([0,0,0,0])
q_crc5 = np.array([1,0,1,1,1])

ack_command = np.array([0,1])
#ack_RC16 = np.array('i',[1,0,1,1,1])

#build header
q_header = np.append(q_command,q_DR)
q_header = np.append(q_header,q_M)
q_header = np.append(q_header,q_TRext)
q_header = np.append(q_header,q_select)
q_header = np.append(q_header,q_target)
q_header = np.append(q_header,q_Q)
q_header = np.append(q_header,q_crc5)
#ack_header = np.append(ack_command,ack_RC16)
#print('header ',q_header)


#endode the header with PIE
coded_header = np.array([],int)
zero = np.array([1,0])
one = np.array([1,1,1,0])
for x in q_header:
    if x == 0:
        coded_header = np.append(coded_header, zero)
        #print(coded_header)
    else:
        coded_header = np.append(coded_header, one)
        #print(coded_header)
    
#print('coded: ',coded_header)
    

#add string of ones for continuouse wave, this lets the tag respond
cw = np.ones(1000) # this is a guese, need MATH
np.append(coded_header,cw)


#write to file, gnuradio will read from this file
file_bits= bytearray(coded_header)
newfile = open('query_bits.b','wb')
newfile.write(file_bits)
newfile.close()

if__name__=="__main__":
    
    main(wave)
    

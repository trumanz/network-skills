import os
import time
from multiprocessing import Process
import multiprocessing as mp

from multicast_receiver import mrecv
from multicast_sender import msend
import logging

FORMAT = '%(process)d %(processName)s %(asctime)s : %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)
 
if  __name__ == '__main__':
    r1 = Process(target=mrecv)
    r2 = Process(target=mrecv)

    r1.start()
    r2.start()

    time.sleep(2)
    msend()
 
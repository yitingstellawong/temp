# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import logging
from logging import handlers
import threading
import os
import time
    
class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }

    def __init__(self, filename, level = 'info', when = 'D', 
                 fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        self.logger.setLevel(self.level_relations.get(level))
        
        format_str = logging.Formatter(fmt)
        sh = logging.StreamHandler()
        sh.setFormatter(format_str) 
        th = handlers.TimedRotatingFileHandler(filename = filename, when = when, encoding = 'utf-8')
        th.setFormatter(format_str)
        
        self.logger.addHandler(sh) 
        self.logger.addHandler(th)


exitFlag = 0
class myThread(threading.Thread):   
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):  
        print_time(self.name, self.counter, 10000)
        
 
def print_time(threadName, delay, counter):
    while counter:
        t1 = time.time()
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        t2 = time.time()
        log.logger.info(threadName + " " + str(round(t2 - t1, 4)))
        counter -= 1
 
      
if __name__ == '__main__':
    folder = os.path.join("C:\\", "tmp")
    if not os.path.exists(folder):
        os.mkdir(folder)
        
    src_folder = "C:\\tmp\\"
    log = Logger(src_folder + 'tmp.log', level = 'debug')
    
    thread1 = myThread(1, "Thread-1", 2)
    thread2 = myThread(2, "Thread-2", 2)
    thread3 = myThread(3, "Thread-3", 2)

    thread1.start()
    thread2.start()
    thread3.start()





    

    
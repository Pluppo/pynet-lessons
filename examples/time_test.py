#! /usr/bin/env python3.6

import time

start_time = time.time()

#Test:
time.sleep(1.2)

elapsed_time = time.time() - start_time

print('Time elapsed: {} seconds'.format(elapsed_time))

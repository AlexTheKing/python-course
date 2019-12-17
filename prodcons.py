import threading
import random
import time

queue = []
lock = threading.Lock()

def go_sleep(name):
	sleep_time = random.random() * 3
	#print('[{0}] Sleeps for: {1} s'.format(name, sleep_time))
	time.sleep(sleep_time)
	

def producer():
	for i in range(0, 10):
		go_sleep('PRODUCER')
		value = random.randint(1, 20)
		print('[PRODUCER] Created object: {0}'.format(value))
		lock.acquire()
		queue.append(value)
		lock.release()
	print('[PRODUCER] Sending termination object')
	lock.acquire()
	queue.append(-1)
	lock.release()

def consumer():
	keep_working = True
	while keep_working:
		go_sleep('CONSUMER')
		lock.acquire()
		if len(queue):
			value = queue.pop(0)
		else:
			lock.release()
			continue
		lock.release()
		keep_working = value != -1
		print('[CONSUMER] Got object: {0}'.format(value))
	print('[CONSUMER] Received termination object')

prod = threading.Thread(target=producer)
cons = threading.Thread(target=consumer)

random.seed(123)

print('Starting producer and consumer')
prod.start()
cons.start()
print('Waiting to get job done')
prod.join()
cons.join()
print('Done')

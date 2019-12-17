from multiprocessing import Process, Queue
import random
import time

queue = Queue()

def go_sleep(name):
	sleep_time = random.random() * 3
	#print('[{0}] Sleeps for: {1} s'.format(name, sleep_time))
	time.sleep(sleep_time)
	
def producer():
	for i in range(0, 10):
		go_sleep('PRODUCER')
		value = random.randint(1, 20)
		print('[PRODUCER] Created object: {0}'.format(value))
		queue.put(value)
	print('[PRODUCER] Sending termination object')
	queue.put(-1)

def consumer():
	keep_working = True
	while keep_working:
		go_sleep('CONSUMER')
		if not queue.empty():
			value = queue.get()
		else:
			continue
		keep_working = value != -1
		print('[CONSUMER] Got object: {0}'.format(value))
	print('[CONSUMER] Received termination object')

prod = Process(target=producer)
cons = Process(target=consumer)

random.seed(123)

print('Starting producer and consumer')
prod.start()
cons.start()
print('Waiting to get job done')
prod.join()
cons.join()
print('Done')


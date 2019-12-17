import threading
import time

def thread_func(name):
	print('Thread {name}: starting'.format(name=name))
	time.sleep(2)
	print('Thread {name}: finishing'.format(name=name))

def create_threads():
	return [threading.Thread(target=thread_func, args=(i,)) for i in range(5)]

print('Before creating')
threads = create_threads();
print('After creating')

for thread in threads:
	thread.start()

print('After start')

for thread in threads:
	print('Joining thread {0}'.format(thread.name))
	thread.join()

print('Done')
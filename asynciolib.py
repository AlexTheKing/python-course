import asyncio
import random

queue = []

async def go_sleep(name):
	sleep_time = random.random() * 3
	#print('[{0}] Sleeps for: {1} s'.format(name, sleep_time))
	await asyncio.sleep(sleep_time)
	

async def producer():
	for i in range(0, 10):
		await go_sleep('PRODUCER')
		value = random.randint(1, 20)
		print('[PRODUCER] Created object: {0}'.format(value))
		queue.append(value)
	print('[PRODUCER] Sending termination object')
	queue.append(-1)

async def consumer():
	keep_working = True
	while keep_working:
		await go_sleep('CONSUMER')
		if len(queue):
			value = queue.pop(0)
		else:
			continue
		keep_working = value != -1
		print('[CONSUMER] Got object: {0}'.format(value))
	print('[CONSUMER] Received termination object')

async def main():
	print('Starting producer and consumer')
	await asyncio.gather(asyncio.create_task(producer()), asyncio.create_task(consumer()))
	print('Done')

random.seed(123)

asyncio.run(main())
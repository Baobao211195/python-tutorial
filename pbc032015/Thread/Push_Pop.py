# co su dung redis
import redis
import logging
import threading
import time



pool = redis.ConnectionPool(host = 'localhost',port = 6379,db = 0)
#logging.basicConfig(format='[%(ThreadName)-10s]',level = logging.DEBUG)
def Push(pool):
	while True:
		r = redis.Redis(connection_pool = pool)
		r.lpush('ten','oanh')
		time.sleep(20)
		
def Pop(pool):
	while True:
		r = redis.Redis(connection_pool = pool)
		print r.rpop('ten')

def main():
	t1 = threading.Thread(target = Push, args =(pool,))
	t2 = threading.Thread(target = Pop, args =(pool,))
	t1.start()
	t2.start()
if __name__ == '__main__':
	main()
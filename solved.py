import threading
import time

class Resource:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

def task(resource1, resource2, thread_name):
    print(f"{thread_name} attempting to acquire {resource1.name}")
    acquired_resource1 = resource1.lock.acquire(timeout=5)
    if acquired_resource1:
      print(f"{thread_name} acquired {resource1.name}")
      time.sleep(1)
      print(f"{thread_name} attempting to acquire {resource2.name}")
      acquired_resource2 = resource2.lock.acquire(timeout=5)
      if acquired_resource2:
        print(f"{thread_name} acquired {resource2.name} and finished work.")
        
        time.sleep(1)
        resource2.lock.release()
      else:
        print(f"{thread_name} could not acquire {resource2.name}")
      resource1.lock.release()
    else:
       print(f"{thread_name} could not acquire {resource1.name}")

    print(f"{thread_name} released resources")


resource_a = Resource("A")
resource_b = Resource("B")

thread1 = threading.Thread(target=task, args=(resource_a, resource_b, "Thread 1"))
thread2 = threading.Thread(target=task, args=(resource_a, resource_b, "Thread 2")) # Changed resource acquisition order

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished")
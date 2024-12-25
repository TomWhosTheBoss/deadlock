import threading
import time

class Resource:
    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

def task(resource1, resource2, thread_name):
    print(f"{thread_name} attempting to acquire {resource1.name}")
    with resource1.lock:
        print(f"{thread_name} acquired {resource1.name}")
        time.sleep(1)
        print(f"{thread_name} attempting to acquire {resource2.name}")
        with resource2.lock:
            print(f"{thread_name} acquired {resource2.name} and finished work.")
           
            time.sleep(1)
    print(f"{thread_name} released both resources.")


resource_a = Resource("A")
resource_b = Resource("B")


thread1 = threading.Thread(target=task, args=(resource_a, resource_b, "Thread 1"))
thread2 = threading.Thread(target=task, args=(resource_b, resource_a, "Thread 2"))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Finished")
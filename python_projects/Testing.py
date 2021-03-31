import threading, time, random

def do_something(sec):
    print(f"sleeping {sec} sec...")
    time.sleep(sec)
    print("done sleeping...")

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[2])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
print()
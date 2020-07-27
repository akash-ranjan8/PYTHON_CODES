import threading
print("current threading is : ",threading.current_thread.getName())
if threading.current_thread()==threading.main_thread():
    print("main threading")
else:
    print("some other threading")
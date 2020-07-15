from threading import Thread
import job1,job2,job3,job4

t1=Thread(target=job1.Job1())
t2=Thread(target=job2.Job2())
t3=Thread(target=job3.Job3())
t4=Thread(target=job4.Job4())


t1.start()
t2.start()
t3.start()
t4.start()

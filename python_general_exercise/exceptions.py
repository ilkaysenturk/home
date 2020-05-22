try:
    f=open("dummy.txt")
    f.write("bla bla")
except:
    print("something went wrong")
finally:
    f.close()

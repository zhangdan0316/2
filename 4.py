import datetime,time
def log(message,when=None):
    when = datetime.datetime.now()
    print ('%s:%s'%(when,message))

log('Hi Python')
time.sleep(1)
log('Hi Pthon again')

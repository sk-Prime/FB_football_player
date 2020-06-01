import mss
import numpy as np
import time

from pymouse import PyMouse
from PIL import Image
from multiprocessing import Process

m = PyMouse()

def run(m,t=685,y=710,color=66):
    global target
    with mss.mss() as sct:
        # The screen part to capture
        monitor = {"top": t, "left": 40, "width": 200, "height": 1}
        output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)
        while True:
            # Grab the data
            time.sleep(0.008)
            sct_img = sct.grab(monitor)
            img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX").convert('L')
            pix=np.array(img).flatten()
            wh = np.where(pix==color)[0]
            if wh.size>1:
                
                #target = int((wh[0]+wh[-1])/2)
                #target=wh[0]+10
                target=wh[int(wh.size/2)]
                print(wh.size,target)
                m.click(target+40,y,1,1)
                time.sleep(0.18)
                #if count>500:
                    #close=True

m1=PyMouse()
m2=PyMouse()
m3=PyMouse()
m4=PyMouse()
p1= Process(target= run,args=(m1,))
p2= Process(target= run, args=(m2,600,630))
p3= Process(target= run, args=(m3,530,560))
p4= Process(target= run, args=(m4,480,510))
p1.start()
p2.start()
p3.start()
p4.start()

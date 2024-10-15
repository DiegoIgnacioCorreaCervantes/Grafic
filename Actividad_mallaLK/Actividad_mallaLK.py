import numpy as np 
import cv2 as cv

cap = cv.VideoCapture(0)


lkparm =dict(winSize=(15,15), maxLevel=2,
             criteria=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03)) 


_, vframe = cap.read()
vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
p0 = np.array([(20,30), (100,30), (200,30), (300,30), (400,30), (500,30), (600,30),
               (20,116), (100,116), (200,116), (300,116), (400,116), (500,116), (600,116),
               (20,202), (100,202), (200,202), (300,202), (400,202), (500,202), (600,202),
               (20,288), (100,288), (200,288), (300,288), (400,288), (500,288), (600,288),
               (20,374), (100,374), (200,374), (300,374), (400,374), (500,374), (600,374),
               (20,460), (100,460), (200,460), (300,460), (400,460), (500,460), (600,460)])

p0 = np.float32(p0[:, np.newaxis, :])

mask = np.zeros_like(vframe) 
cad =''

while True:
    _, frame = cap.read()
    fgris = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    p1, st, err = cv.calcOpticalFlowPyrLK(vgris, fgris, p0, None, **lkparm) 

    if p1 is None:
        vgris = cv.cvtColor(vframe, cv.COLOR_BGR2GRAY)
        p0 = np.array([(100,100), (200,100), (300,100), (400,100) ])
        p0 = np.float32(p0[:, np.newaxis, :])
        mask = np.zeros_like(vframe)
        cv.imshow('ventana', frame)
    else:
        bp1 = p1[st ==1]
        bp0 = p0[st ==1]
        
        for i, (nv, vj) in enumerate(zip(bp1, bp0)):
            a, b = (int(x) for x in nv.ravel())
            c, d = (int(x) for x in vj.ravel())
            dist = np.linalg.norm(nv.ravel() - vj.ravel())

            #print(i, dist)
            
            
            
            frame = cv.line(frame, (c,d), (a,b), (0,0,255), 2)
            frame = cv.circle(frame, (c,d), 2, (255,0,0),-1)
            frame = cv.circle(frame, (a,b), 3, (0,255,0),-1)
        cv.imshow('ventana', frame)

        vgris = fgris.copy()

        if(cv.waitKey(1) & 0xff) == 27:
            break

cap.release()
cv.destroyAllWindows()



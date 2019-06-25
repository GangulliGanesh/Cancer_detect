def Extract_X(path):
    import os
    import csv
    import numpy as np
    j=[]
    with open(path,'r') as file:
        reader = csv.reader(file,delimiter=' ')
        for a,b in reader:
            j.append(a)
            j.append(b)
            kl=np.asarray(j)

    klm=int(len(kl)/2)
    data=np.reshape(kl,(klm,2))
    data=np.array(data,dtype=np.int32)
    ax=np.zeros((klm))
    for i in range(klm):
        ax[i]=data[i][0]

    return ax

def Extract_Y(path):
    import os
    import csv
    import numpy as np
    j=[]
    with open(path,'r') as file:
        reader = csv.reader(file,delimiter=' ')
        for a,b in reader:
            j.append(a)
            j.append(b)
            kl=np.asarray(j)

    klm=int(len(kl)/2)
    data=np.reshape(kl,(klm,2))
    data=np.array(data,dtype=np.int32)
    ax=np.zeros((klm))
    for i in range(klm):
        ax[i]=data[i][1]

    return ax

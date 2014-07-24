import numpy as np
import scipy.io as sp
import matplotlib.pyplot as mpt
import scipy.fftpack.pseudo_diffs as hil
a=sp.loadmat("/media/raja/raja/chmit/chb06_01_edfm.mat")
b=a['val']
c=b[1]
d=c[441344:444928]
f={"mat":d}
sp.savemat("/media/raja/raja/chmit/chb06_01_edfm_seizure1.mat",f)
g=sp.loadmat("/media/raja/raja/chmit/chb06_01_edfm_seizure1.mat")
h=g['mat']
i=hil.hilbert(h)



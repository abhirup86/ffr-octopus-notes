import numpy as np
import matplotlib.pyplot as plt
import sys

plt.clf()
for ii in range(5):
    filname = "static/wf-st000" + str(ii+1) + ".y=0,z=0"
    wf = np.loadtxt(filname)
    sys.stdout.write("file: %s is read\n" % filname)
    lbl = "wfs-" + str(ii)
    plt.plot( wf[:,0], wf[:,1], label=lbl )
#
plt.legend()
plt.grid()
plt.savefig("wfs.pdf")

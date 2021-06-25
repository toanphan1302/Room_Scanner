import numpy as np

def convert(sphr):
    '''
    Input: sphr nx3 np.array
    ***********
    Output: x,y,z
    '''

#    sphr = np.empty([3, 2]) #don't want to use this? just want to use in input sphr?

    r = sphr[0]
    theta = sphr[1]
    phi = sphr[2]

    x = list()
    y = list()
    z = list()

    # convert from spherical to cartersian through list
    i = 0
    while i < len(r):
        x.extend([r[i]*np.sin(phi[i]*np.pi/180)*np.cos(theta[i]*np.pi/180)])
        y.extend([r[i]*np.sin(phi[i]*np.pi/180)*np.sin(theta[i]*np.pi/180)])
        z.extend([r[i]*np.cos(phi[i]*np.pi/180)])
        i = i + 1

    xyz = [x,y,z]
    return xyz

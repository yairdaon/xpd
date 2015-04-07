import numpy as np


def inv(P):
    '''
    invert 2x2 matrix
    '''
    inv = np.zeros( (2,2) )
    
    inv[0,0] =  P[1,1]
    inv[1,1] =  P[0,0]
    inv[1,0] = -P[1,0]
    inv[0,1] = -P[0,1]
    det = P[0,0]*P[1,1] - P[1,0]*P[0,1]
    if det < 0:
        print "ahhhhhh"
    return inv, det



r = 0.5 # rho
s = 0.2 # sigma square
print #(  "Rho = " + str(r) +  ", sig^2 = " +  str(s))

# the covariance matrix we have
covariance = np.array([  [ 1  ,  r  ,  1    ,   1    ,  r    ] ,
                         [ r  ,  1  ,  r    ,   r    ,  1    ] ,
                         [ 1  ,  r  ,  1+s  ,   1    ,  r    ] ,
                         [ 1  ,  r  ,  1    ,   1+s  ,  r    ] ,
                         [ r  ,  1  ,  r    ,   r    ,  1+s  ]
                         ])

                
# Consider the case where we have two observatuions at first point

A  = covariance[0:2,0:2]
B  = covariance[2:4,2:4]
C  = covariance[0:2, 2:4]
iB , det = inv(B) 

#post_cov = (A*det - C*iB*np.transpose(C)  ) /  det

#post_var = post_cov[0,0] + post_cov[1,1]
post_var  = s*(s+1-s*r*r)/(s*s +2*s+1 -r*r)
print("Measeure x_1 twice, the posterior variance is " +
      str(post_var) )


# Now consider the case where we take two observations at x_1 and  x_2

# A stays the same


B = np.array([ [ 1+s  , r   ] , 
               [ r    , 1+s ] ]
             )

C = np.array( [[ 1 , r ] ,
               [ r , 1 ] 
               ])

iB , det = inv(B) 
#post_cov = ( A*det - C*iB*np.transpose(C) )  /  det

#post_var = post_cov[0,0] + post_cov[1,1]
post_var = 2 -2*(1+r*r)/(2+s)
print("Measeure x_1 and then x_2, the posterior variance is " +
      str(post_var) )

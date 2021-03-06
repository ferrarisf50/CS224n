#!/usr/bin/env python

import numpy as np
import random

from q1_softmax import softmax
from q2_sigmoid import sigmoid, sigmoid_grad
from q2_gradcheck import gradcheck_naive

#%%
def forward_backward_prop(data, labels, params, dimensions):
    """
    Forward and backward propagation for a two-layer sigmoidal network

    Compute the forward propagation and for the cross entropy cost,
    and backward propagation for the gradients for all parameters.

    Arguments:
    data -- M x Dx matrix, where each row is a training example.
    labels -- M x Dy matrix, where each row is a one-hot vector.
    params -- Model parameters, these are unpacked for you.
    dimensions -- A tuple of input dimension, number of hidden units
                  and output dimension
    """

    ### Unpack network parameters (do not modify)
    ofs = 0
    Dx, H, Dy = (dimensions[0], dimensions[1], dimensions[2])

    W1 = np.reshape(params[ofs:ofs+ Dx * H], (Dx, H))
    ofs += Dx * H
    b1 = np.reshape(params[ofs:ofs + H], (1, H))
    ofs += H
    W2 = np.reshape(params[ofs:ofs + H * Dy], (H, Dy))
    ofs += H * Dy
    b2 = np.reshape(params[ofs:ofs + Dy], (1, Dy))

    ### YOUR CODE HERE: forward propagation
    x1=np.dot(data,W1)+b1     #   (M,Dx).(Dx,H)+(1,H)=(M,H)
    h=sigmoid(x1)             #   (M,H)
    x2=np.dot(h,W2)+b2        #   (M,H).(H,Dy)+(1,Dy)=(M,Dy)
    yhat=softmax(x2)          #   (M,Dy)
    cost=-np.mean(np.sum(np.log(yhat)*labels))          #  (M,Dy)*(M*Dy)=(M*Dy) sum in all scalar
    
    ### END YOUR CODE

    ### YOUR CODE HERE: backward propagation
    
    ### END YOUR CODE
    d1=yhat-labels       # (M,Dy)-(M,Dy)=(M,Dy)
    gradb2=np.sum(d1,axis=0)      # sum all row (M,Dy)->(1,Dy)
    gradW2=np.dot(h.T,d1)    # (H,M).(M,Dy)=(H,Dy)
    
    d2=np.dot(d1,W2.T)*sigmoid_grad(h)   # (M,Dy).(Dy,H)*(M,H)=(M,H)
    
    gradb1=np.sum(d2,axis=0)      # (1,H)
    gradW1=np.dot(data.T,d2)        # (Dx,M).(M,H)=(Dx,H)
    
    ### Stack gradients (do not modify)
    grad = np.concatenate((gradW1.flatten(), gradb1.flatten(),
        gradW2.flatten(), gradb2.flatten()))

    return cost, grad


def sanity_check():
    """
    Set up fake data and parameters for the neural network, and test using
    gradcheck.
    """
    print ("Running sanity check...")

    N = 20
    dimensions = [10, 5, 10]
    data = np.random.randn(N, dimensions[0])   # each row will be a datum
    labels = np.zeros((N, dimensions[2]))
    for i in range(N):
        labels[i, random.randint(0,dimensions[2]-1)] = 1

    params = np.random.randn((dimensions[0] + 1) * dimensions[1] + (
        dimensions[1] + 1) * dimensions[2], )

    gradcheck_naive(lambda params:
        forward_backward_prop(data, labels, params, dimensions), params)


def your_sanity_checks():
    """
    Use this space add any additional sanity checks by running:
        python q2_neural.py
    This function will not be called by the autograder, nor will
    your additional tests be graded.
    """
    print ("Running your sanity checks...")
    ### YOUR CODE HERE
    #raise NotImplementedError
    ### END YOUR CODE


if __name__ == "__main__":
    sanity_check()
    your_sanity_checks()

    
#%%
aaa=np.array([[1,2],[3,4]])
aaa1=np.array([1,2])
print(aaa+aaa1)
print(np.dot(aaa,aaa1))
print(np.mean(aaa))
print(np.sum(aaa,axis=0))

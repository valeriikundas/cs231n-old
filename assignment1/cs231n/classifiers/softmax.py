import numpy as np
from random import shuffle
#from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = np.dot(X, W)
  num_train = X.shape[0]
  num_classes = W.shape[1]
  
  for i in range(num_train):
    bottom = 0.0
    for j in range(num_classes):
        bottom += np.exp(scores[i, j])
            
    loss += -np.log(np.exp(scores[i, y[i]]) / bottom)
        
    for j in range(num_classes):
        if j == y[i]:
            dW[:, y[i]] += X[i] * (-1 + np.exp(scores[i, y[i]]) / bottom)
        else:
            dW[:, j] += X[i] * np.exp(scores[i, j]) / bottom
        
  loss /= num_train
  loss += reg * np.sum(W * W)
  dW /= num_train
  dW += 2 * reg * W
    
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  scores = np.dot(X, W)
  num_train = X.shape[0]
  num_classes = W.shape[1]
  
  bottom = np.sum(np.exp(scores), axis=1)

  coef = np.exp(scores) / bottom.reshape(-1, 1)
  coef[range(num_train), y] -= 1
  
  loss = np.sum(-np.log(np.exp(scores[range(num_train), y]) / bottom))
  loss /= num_train
  loss += reg * np.sum(W * W)

  dW = np.dot(X.T, coef) / num_train + 2 * reg * W      
  
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


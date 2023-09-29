import numpy as np
#creste a sample matrix
X =np.array([[1,2,3],[4,5,6],[7,8,9]])
#Perform SVD
U,S,VT =np.linalg.svd(X)
#choode the number of component to keep (eg.2)
n_components=2
# reconstructed the matrix with reduced dimentions
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original Matrix:")
print(X)
print("\nReconstructed Matrix (with reduced dimensions):")
print(X_reconstructed)
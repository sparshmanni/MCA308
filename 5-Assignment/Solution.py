import numpy as np
from scipy.spatial import distance

#Q1

customer_A = [4,5,2,3,4]
customer_B = [5,3,2,4,5]
customer_A_binary = [1,0,1,1,0,1]
customer_B_binary = [1,1,1,0,0,1]

# Euclidean Distance
print("Euclidean distance : ",distance.euclidean(customer_A,customer_B))

# Manhattan Distance
print("Manhattan distance : ",distance.cityblock(customer_A,customer_B))

# Cosine Similarity
print("Cosine distance : ",distance.cosine(customer_A,customer_B))

# Hamming Distance
print("Hamming distance : ", distance.hamming(customer_A_binary, customer_B_binary))

# Jaccard Similarity (for binary)
A = np.array(customer_A_binary)
B = np.array(customer_B_binary)

intersection = np.sum((A == 1) & (B == 1))
union = np.sum((A == 1) | (B == 1))

jaccard = intersection / union
print("Jaccard:", jaccard)


# Q2 data

user1 = [5, 3, 4, 4, 2]
user2 = [4, 2, 5, 4, 3]

# Chebyshev Distance
print("Chebyshev:", distance.chebyshev(user1, user2))

# Minkowski Distance (p=3)
print("Minkowski (p=3):", distance.minkowski(user1, user2, 3))
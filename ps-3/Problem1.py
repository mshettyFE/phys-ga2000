import numpy as np
import time

Iters = 20

def explicitMatMul(NumIters):
    starting_size = 10
    Matrix_size = []
    time_taken = []
    for iteration in range(NumIters):
        # Generate starting matrices
        N = starting_size+iteration*10
        A = np.random.rand(N,N)
        B = np.random.rand(N,N)
        C = np.zeros([N,N], dtype=np.float32)
        # Only time computation
        t1 = time.time()
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    C[i,j] += A[i,k]* B[k,j]
        # Finish timing and note results
        t2 = time.time()
        Matrix_size.append(N)
        time_taken.append(t2-t1)
    return Matrix_size, time_taken
                    

def dotMatMul(NumIters):
    starting_size = 10
    Matrix_size = []
    time_taken = []
    for iteration in range(NumIters):
        # Generate starting matrices
        N = starting_size+iteration*10
        A = np.random.rand(N,N)
        B = np.random.rand(N,N)
        # Only time computation
        t1 = time.time()
        C = np.dot(A,B)
       # Finish timing and note results
        t2 = time.time()
        Matrix_size.append(N)
        time_taken.append(t2-t1)
    return Matrix_size, time_taken
 
def crappyCSVGeneration(left, right, fname):
    assert(len(left) == len(right))
    with open(fname+".csv", 'w') as f:
        for i in range(len(left)):
            f.write(str(left[i]))
            f.write(",")
            f.write(str(right[i]))
            f.write("\n")

if __name__ == "__main__":
    size, t = explicitMatMul(Iters)
    crappyCSVGeneration(size, t, "Explicit")
    size_dot, t_dot = dotMatMul(Iters)
    crappyCSVGeneration(size_dot, t_dot, "Dot")



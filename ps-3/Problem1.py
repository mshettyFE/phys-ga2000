import numpy as np
import matplotlib.pyplot as plt
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
 
if __name__ == "__main__":
    size, t = explicitMatMul(Iters)
    size_dot, t_dot = dotMatMul(Iters)
    fig, (ax1, ax2) = plt.subplots(1,2, sharey=True)
    ax1.plot(size,t, color = 'b')
    ax1.set_title("Standard")
    ax1.set_xlabel("Mat Size")
    ax1.set_ylabel("Time (s)")
    ax1.set_yscale("log")
    ax1.set_xscale("log")
    
    ax2.plot(size_dot,t_dot)
    ax2.set_title("Dot")
    ax2.set_xlabel("Mat Size")
    ax2.set_ylabel("Time (s)")
    ax2.set_yscale("log")
    ax2.set_xscale("log")
    
    fig.tight_layout()
    plt.show()

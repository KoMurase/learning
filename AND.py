import numpy as np

xs = np.array([[0,0],[0,1],[1,0],[1,1]], dtype = np.float32)
ts = np.array([[-1],[-1],[-1],[1]], dtype = np.float32)
print(xs)
print(ts)
np.random.seed(0)

# perceptron
w = np.random.normal(0.,1,(3))
print(w)

#add bias
_xs = np.hstack([xs , [[1] for _ in range(4)]])
#hstackで水平方向に連結
print('_xs>>',_xs)
for i in range(4):
    ys = np.dot(w, _xs[i])
    print("in >>", _xs[i],"y >>",ys)

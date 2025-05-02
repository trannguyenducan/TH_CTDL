import torch
import torch.nn as nn

class Softmax:
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition1 = x_exp.sum(0, keepdims=True)
        return x_exp / partition1
    
class Softmax_stable:
    def __init__(self):
        super().__init__()

    def forward(self, y):
        y_max = torch.max(y, dim=0, keepdims=True)
        y_exp = torch.exp(y - y_max.values)
        partition2 = y_exp.sum(0, keepdims=True)
        return y_exp / partition2    
# Examples 1
data = torch.tensor([1, 2, 3])
softmax = Softmax()
output = softmax.forward(data)
print("Softmax Output:", output)

data = torch.tensor([1, 2, 3])
softmax_stable = Softmax_stable()
output_stable = softmax_stable.forward(data)
print("Softmax Stable Output:", output_stable) 
# autograd example
import torch

#create an input
x = torch.rand(2,requires_grad=True)
print(x)

y=x+2
print(y)

z=y*y
print(z)

v = torch.mean(z)
print(v)

print(x.grad)
z.backward()
print(x.grad, y.grad)
## 向量求导  
  [求导公式](https://blog.csdn.net/lipengcn/article/details/52815429)  
  [视频链接：李沐](https://www.bilibili.com/video/BV1eZ4y1w7PY?from=search&seid=4070688631110788090&spm_id_from=333.337.0.0)  
  
## 自动向量求导  
```python  
from mxnet import autograd, nd
with autograd.record():
  a = nd.ones((2, 1))
  b = nd.ones(2, 1))
  c = 2 * a + b
  ```  
  ### 计算图  
    1将代码分解成操作子  
    2将计算表示成无环图  
    3.1显示构造: tensorflow/Theano/MXNet  
    3.2隐式构造：PyTorch/MXNet
 ### 自动求导的两种模式 
    例如：z = (<x,w>-y)^2 : 令b=<x,w>-y a=<x,w>
    1 正向累积a->b->z 先求partial(a)/partial(w)，然后一步步求，和递归很像。
    2 反向累积z->b->a 这里先求partial(z)/partial(b), 然后求partial(z)/partial(a)，在这里partial(z)/partial(a)=partial(z)/partial(b)*partial(b)/partial(a)，显然要利用到前一步的结果。  
    关于这里的方向没太懂，就我理解而言的Backpropagation, 是不需要中间参数的，和这里的正向累积一致，怀疑正反向反了。
  ## 自动求导codes
  ```python
  x = torch.arange(4.0)
   #find a space to save teh grad, so you can easily print the grad by x.grad. Of course, it is equallent to x = torch.arange(4.0, requires_grad=True
  x.requires_grad_(True)
  y = x * x
   #等价y.backward(torch.ones(len(x))
  y.sum().backward() 
  x.grad
  ```
  ```python
 tensor([0.,2.,4.,6.,])
 ```
    torch.ones(3, 4)就是创建一个3*4的tensor   
    x.grad.zero_()就是对grad全赋值0  
     .sum()操作其实是将向量求导转化为标量求导，深度学习中大多数都是转化为标量在操作求导
     
   ## 回归预测
   线性回归是对n维输入的加权，外加偏差
    使用平方损失来衡量预测值和真实值的差异
    线性回归有显示解，一般深度学习解决的问题都很复杂，是模型自己训练出来函数去达到我们的目的，很难自己构造函数。
    线性回归可以看作是单层神经网络
    
   ## 关于损失求平均值  
   
   ![](http://latex.codecogs.com/svg.latex?W_{t}=W_{t-1}-\eta\frac{\partial{l}}{\partial{W_{t-1}}})
   如果在loss里面没有除以batch_size，最后在loss里面就是nloss，求导之后也会多出n。
   **现在才发现是通过loss达到最优去寻找合适的函数，是对loss求导，然后更改features**
    

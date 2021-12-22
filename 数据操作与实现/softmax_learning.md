### 几类loss
####  L2loss
![](http://latex.codecogs.com/svg.latex?l(y,y')=\frac{1}{2}(y-y')^2)
#### L1loss
![](http://latex.codecogs.com/svg.latex?l(y,y')=|y-y'|)
#### Huber's Robust Los
![robust loss](https://github.com/pipiyea287/ubuntu_git_file/blob/main/picture/robust%20loss.gif)
### the sum of torch
```python
X = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0,6.0]])
X.sum(0, keepdim=True),  X.sum(1, keepdim=True)
```  
第一个参数应该是加到维度上， 第二个参数是保证输入输出维度是一致的。
### cross entropy
香农提出entropy是保证信息传递无误的最小平均编码长度



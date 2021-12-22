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
![](http://latex.codecogs.com/svg.latex?entropy=-\sum_{i}{P(i)\log_2{P(i)})  
其实可以和求期望联系起来，概率乘以相应的编码长度，复杂度为N，则发生其中一种为1/N，而编码长度为![](http://latex.codecogs.com/svg.latex?\log_2{N}=\log_2{\frac{1}{P}=-\log_2{P(i))  
考虑到真实的P不知道，所以选用观测到的Q进行计算，但是![](http://latex.codecogs.com/svg.latex?entropy=-\sum_{i}{Q(i)\log_2{Q(i)})，一旦Q是错误的，会影响二者，导致比较大的错误。所以引入cross entropy,![](http://latex.codecogs.com/svg.latex?crossentropy=-\sum_{i}{P(i)\log_2{Q(i)}).  
在损失函数中，采用one-hot encoding，可以使用cross entropy,累加其实就变成单纯的对正确预测概率的计算，其余都是0\*log_2{Q}.如果是二分类预测，那就更简单了，变成2个相加，不需要用累加了。


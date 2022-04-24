### the difference between F.ReLU and nn.ReLU
[explanation](https://blog.csdn.net/Caesar6666/article/details/108035105)   
when you use F.ReLu to define the ReLu layer, it will not pirnt the layer name and type if you try output the layer name. 
### resnet
resnet is a useful network for solving gradient relative problems, like gradient vanish or explosion. 
It is because of the residual path, by using this path, all the layers just like going through a fast speed road to get a propel gradient value.  
Remember the formula: y = f(x) + g(f(x))
### CrossEntropy loss
For CrossEntropy loss, 

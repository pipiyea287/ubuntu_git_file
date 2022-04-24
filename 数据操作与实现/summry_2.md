### the difference between F.ReLU and nn.ReLU
[explanation](https://blog.csdn.net/Caesar6666/article/details/108035105)   
when you use F.ReLu to define the ReLu layer, it will not pirnt the layer name and type if you try output the layer name. 
### resnet
resnet is a useful network for solving gradient relative problems, like gradient vanish or explosion. 
It is because of the residual path, by using this path, all the layers just like going through a fast speed road to get a propel gradient value.  
Remember the formula: y = f(x) + g(f(x))
### CrossEntropy loss
For CrossEntropy loss,   
![](http://latex.codecogs.com/svg.latex?l=\sum_{i}{p_{i}\log{q_{i}}}) 
Inside this formula, p_i denotes the value of the given label y, while q_i is the predicted value. For this formula, the less the value is, the more accurate the prediction is.   And note that the q_i is transformed by softmax.
  To  reduce the effect of the real tables, we introduce the smoothing label and the improved formula is as follows:  
    ![](http://latex.codecogs.com/svg.latex?y_{i}=1-\alpha)  *if i = target*    
    ![](http://latex.codecogs.com/svg.latex?y_{i}^{'}=\frac{\alpha}{K})       *otherwise*    
      
 

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
    scatter_: a functuion for reordering as the sequence of index. It assigns a dimension, and the value will not change in its.
### data-augmentation
for data agumentation, remember that it needs to fit the real environment. For example,  detecting a object whether is a cat or not, it is difficult to get a image with upside down cat.   
  The main purpose of the augmentation is to get more data that fits the real scene, in another way, geting more images that are the same as the image in test dataset. You need always think about the possible things that will be met in the real use scenarios.
 ###how to write a pytorch dataset
 [process](https://zhuanlan.zhihu.com/p/35698470)
 ### lambda in python
 [intraoduction](https://blog.csdn.net/zjuxsl/article/details/79437563)
### an interesting interpretation for momentum gradient descent.
[interpredation](https://www.zhihu.com/question/24529483)  
  ![](http://latex.codecogs.com/svg.latex?x=x+v )  
    ![](http://latex.codecogs.com/svg.latex?v=\beta*v-\alpha*dx)   
      if the former v and latter v are in the same direction,  it is just like there is a momentum impulse increasing the change of x, and of course, x will converge faster.
### momentum decay and learning rate decay
[interpretation](https://blog.csdn.net/program_developer/article/details/80867468)
### the method to change  numpy to list.
1 change numpy to list: a.tolist()  
  2 convert list to numpy: np.array(a)
###  method for fast loading the pretrained parameters into the model
[link](https://blog.csdn.net/t20134297/article/details/103885879)



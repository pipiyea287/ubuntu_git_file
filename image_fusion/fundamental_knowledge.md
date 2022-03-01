<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
## 采样  
### 上采样  
放大图像，使用内插值，在原有图像像素的基础上采用合适的插值算法插入新值。  
### 下采样  
缩小图像，使得图像;1符合显示区域的大小，2生成对应图像的缩略图  

***图像高频信息就是轮廓，此处图像不连续，变化大。Laplace 就是通过做差分保留了这些高频信息*** 

[公式编辑](https://www.jianshu.com/p/25f0139637b7)

## Gauss pyramid  
  金字塔0层为原始图，新层通过高斯滤波和对下一层的1/2采样(去掉偶数行、列)
![Gauss Pyramid](https://upload-images.jianshu.io/upload_images/1817489-e6c2eb285bc47352.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)  
## Laplacian Pyramid  
  在进行Gauss pyramid时，高斯滤波（使图像更平滑）和下采样，丢失了很多高频信号。Laplacian pyramid的目的就是保存高频信号，方法是通过保存差分图像保存高频信号。比如其第0层就是原始图像和原始图像下采样后再上采样之后的差值  
  ![Laplacian pyramid](https://upload-images.jianshu.io/upload_images/1817489-942d30565e99358c.png?imageMogr2/auto-orient/strip|imageView2/2/w/992/format/webp)
## 目前看到的很多概念
  轮廓波(contourlet)、曲波(curvelet)、平移不变性（位移方差）(shift invariance)，aliasing（混叠），shearlet（剪切）  
## 剪切波
这方面资料比较少，找到的资料感觉也非常专业，没有通俗性的解释。
## over-complete dictionary
    using with fat matrix(sparse matrix), for orthogonal base , it is solomnly asked and simple. For fat matrix, there are excessive columns to portray the image. Further more, the noise can't be descaibed with sparse base.  
### panchromatic image and intensity component
这部分暂时还不太知道
### morphological analysis
这里是NLP自然语言处理的一个任务，形态分析，具体是对单词的词态进行分析，分析它是由什么组成，词干、词缀等等
### wavelet
傅里叶变换适合平稳信号，使用正弦波模拟信号。但是对于非平稳信号，傅里叶变换没有办法体现出区别，容易因为频率的相近而体现不出区别。短时傅里叶变换，通过选择一个小框解决了部分时间分辨率较低的问题，但是选择多大的框是个难题。而小波变换同时具有时间和频率的高分辨率，适用于非平稳信号，而且对于突变信号，只有突变信号和小波函数重叠时，系数不为零。同时小波变换具有许多不同类型的小波。
[wavelet](https://www.jianshu.com/p/6861539f6c3f)
### image registration
   对于一组图像数据集中的两幅图像，通过一种空间变换把一幅图像（浮动图像 moving image）映射到另一幅图像（fixedimage，参考图像）上，使得两图中对应于空间同一位置上的点一一对应起来，从而达到信息融合的目的。  
   image registration 通常是图像融合的一个预处理步骤，经过精确图像配准的图像对，通常可获得更好的融合效果。
### 马佳义
[马佳义的一些成果](https://blog.csdn.net/baidu_40840693/article/details/103767747)
### 多尺度几何分析
[简略介绍](https://blog.csdn.net/jbb0523/article/details/42689465)
### 图像融合的一些论文，关于可见光和红外光
[论文总结](https://blog.csdn.net/m0_37933882/article/details/107613719)
### patch的概念
pacth就是kernel，卷积神经网络中的概念，每次对一个patch操作。
### 关于Gauss pyramid: up sampling and down sampling and Laplacian Pyramid 
[interpretaion](https://bianhaunzhuanlan.zhihu.com/p/80362140)
### pseudo-Gibbs phenomenon
图像的傅里叶变换 ，由于其变换本身有多种成熟的快速算法（FFT算法），而且性能接近于最佳，从而获得较早的也比较广泛的研究。它的不足之处在于：相邻子图像数据在各个边界不连续造成的所谓Gibbs现象。这是由于图像数据的二维傅里叶变换实质上是一个二维图像的傅立叶展开式。这个二维图像应被认为是周期性的。由于子图像的变换系数在边界不连续 ，而将造成复原的子图像在其边界也不连续 。于是由复原子图像构成的整幅复原图像将呈现隐约可见的以子图像尺寸为单位的方块状结构，影响整个图像质量 。当子图像尺寸较小时更为严重。
### NSCT
[interpretation](https://www.cnblogs.com/wxl845235800/p/12178756.html)
### shift varience
[interpretation(]https://www.cnblogs.com/fydeblog/p/11083664.html)  
in this article, it propose a very simple instance to illustrate the shift invarience. unlike max pooling, to preserve the shift invarience, it join the step of blur, like Gaussian filter to make it smoother, so it avoid shift exquitely.
### sparse representation
[easy_understand_interpretation](https://zhuanlan.zhihu.com/p/151901026)  
sparse representation is found in humen' visual system. We just use few but complete features to recognize a person. So in machine learning, we do not need so many features that they are over-complete for  recognizing. In contrary, we use sparse representation and compose them in a dictionary that is over-completed.In other words, the more complete the dictionary is, the fewer coefficinets we need. Furthermore, the dictionary we can learning from the huge dataset,.Then by a common dictionary, we just need the position of the representation in the dictionary to encode in the process。 When output, decode the position information with the dictionary. So we enhance the efficient of the computation.
## You really need put prmium on the logic of  your eassy when you are writing, otherwise it will be  incoherent sentances which are difficult for understanding.
### multi-scale transform
对于不同大小的图片，往往需要不同的尺度去描述。对于较小的图片就需要高分辨率，而对于较大的图片，就不需要高分辨率，而仅仅通过低分辨率关注轮廓即可。而当一张图片有不同大小的图片时，多尺度就具有更大的优势。  
图像的尺度是指图像内容的粗细程度。尺度的概念是用来模拟观察者距离物体的远近的程度。 具体来说，观察者距离物体远，看到物体可能只有大概的轮廓；观察者距离物体近，更可能看到物体的细节，比如纹理，表面的粗糙等等。从频域的角度来说，图像的粗细程度代表的频域信息的低频成分和高频成分。 粗质图像代表信息大部分都集中在低频段，仅有少量的高频信息。细致图像代表信息成分丰富，高低频段的信息都有。

尺度空间分为线性尺度空间和非线性尺度空间。这里仅讨论线性尺度空间。

在数学上，空间(space)是指具有约束条件的集合(set)。图像的尺度空间是指同一张图像不同尺度的集合。在该集合中，细尺度图像通过filter形成粗尺度图像，即粗尺度图像的形成过程是高频信息被过滤的过程，不会引入新的杂质信息，因此任何存在于粗尺度图像下的内容都能在细尺度图像下找到。举个例子，如果你想看一颗树而不是叶子，可以故意删除图像中的某些细节（例如树叶树枝等），在摆脱这些细节时，必须确保不引入新的虚假细节。做到这一点的唯一方法是使用高斯模糊（已通过数学证明）。  
尺度和分辨率不是划等号的关系，尺度是通过高斯模糊来降低的
获取这种多尺度，一般采用金字塔，比如高斯金字塔，拉普拉斯金字塔等
[easy_understanding_interpretation](https://blog.csdn.net/weixin_43026262/article/details/103138098)
### 图像的高频和低频信息
图像的频率：衡量灰度值变化剧烈程度的指标，是灰度在平面空间上的梯度。  
高频就是灰度梯度变化大，因此边缘检测保存的就是高频信息。  
图像的高频：梯度变化大的地方，比如图像的边缘（laplace pyramid,就是通过差分保存了这种高频信息，包含了细节信息。  
图像的低频：高频轮廓内的变化缓慢的地方。  
多尺度变化中，随着金字塔的层层向上，其实就是保留了图像的低频信息。
### K-SVD
[interpretation](https://blog.csdn.net/liudingbobo/article/details/78490384)  
for the K-SVD is a method to get the best sparse representation.
### infrared and visible image fusion:RFN-Nest: An end-to-end residual fusion network for infrared and visible images
[paper_link](https://zhuanlan.zhihu.com/p/387858991)
### something about the weavelet transform
![weavelet](https://upload-images.jianshu.io/upload_images/23662232-d2d8b8f67a61e0e6.png?imageMogr2/auto-orient/strip|imageView2/2/format/webp)  
from the picture above, we can find that weavelet has better locality about time compared to sine.
### weavelet transform 
[popular and easy to understand](https://zhuanlan.zhihu.com/p/22450818)  
there are 2 dimensions signals in image which is not easy for wavelet transform that is adapt at processing 1 dimension signals.
### image pyramid
[gauss laplace pyramid](https://zhuanlan.zhihu.com/p/80362140)
### prooblem with gradient vanish, ReLU, leaky ReLU
[easy to understand](https://zhuanlan.zhihu.com/p/427541517)
### 2D-wavelet transform
[simple explanation](https://blog.csdn.net/daisy9212/article/details/49184271)
[explanation_2](https://zhuanlan.zhihu.com/p/356794989)
### the difference between edge and boundary
[easy to understand](https://www.zhihu.com/question/314914894)    
    对于一个二维图像，本身有边界xy（boundary），而如果把每个像素的灰度值当作h，得到一个三维图像，这图像的边沿即是edge。

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

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

***图像高频信息就是轮廓，此处图像不连续，变化大。Laplace 就是通过做擦汗保留了这些高频信息*** 

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
  


### F.conv2d, including the dilation
[interpretation](https://blog.csdn.net/weixin_38145317/article/details/104923015)
### denseblock
[densenet](https://zhuanlan.zhihu.com/p/37189203)   
    densenet 如何实现的稠密连接，这点还不是很清楚，另外也可以跑一跑denseblock的代码，沐神那里应该有可以现成使用的。
### debug
[introduction](https://blog.csdn.net/liu201812/article/details/107620068)
### convolutional kernel
to correct some opinions before, the convolutional kernel size is matched to the size of input matrix. So if the matrix is 3 dimensions, the kernel size is also the same. And to get the               multi-channel output, the kernel size generally has one more dimension than the input matrix. 
### model save
[explaination](https://www.ylkz.life/deeplearning/p12977315/)
### tqdm 
it can display the progress bar.
### tensor
[interpretation](https://jishuin.proginn.com/p/763bfbd6ddd0)
### VGG
[easy understanding](https://zhuanlan.zhihu.com/p/41423739)
In VGG, the kernel 5 * 5 is replaced by 2 3 * 3 kernel for the same receptive field size they have.  这是因为他们是级联的，在第二层的3 * 3 核需要第一次层移动三次，每移动一次，能得到第二层的一个点，铺满整个第二层的一行需要三次移动，这就相当于5 * 5的核，可以画出来，便于理解。
### the calculation way for convolution layer and full connected layer parameters.
[explanation](https://zhuanlan.zhihu.com/p/77471991)
### about the python matiplot
[explanation](https://zhuanlan.zhihu.com/p/33270402)
### NiN block
The major in NiN block is using the 1 * 1 conv2d to replace the linear layer, so it avoids the huge parameters well created by full connected layer well. And because of the 1 * 1 conv2d, until the last block, it need utilize the adaptiveAvgpooling layer to change the height and width to 1, so in the next step,  you just need flatten it to 10 dims vector to complete the classification tasks.
### BN layer
It is used to adjust the distribution of the samples to avoild the gradient vanish or explosion. For 1 * 1 conv layer, it effects on the channel dims. And to full connected layer, it acts on the features. It is always put on the front the ReLU layer, because all the samples will be changed to positive after the ReLU layer and it is contradicted with the goal of the BN layer which is used to uniform the sample distributions. 
2,  

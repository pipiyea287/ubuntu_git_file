import torch
from torch import nn
from d2l import torch as d2l
import os

net_save_dir = "/home/iderea/下载/ubuntu_git_file/code_vs"
def vgg_block(num_convs, in_channels, out_channels):
    layers = []
    #this is a convolution block
    for _ in range(num_convs):
        #I think that this is a list, not just a number
        layers.append(nn.Conv2d(in_channels, out_channels,
                                kernel_size=3, padding=1))
        layers.append(nn.ReLU())
        in_channels = out_channels
    layers.append(nn.MaxPool2d(kernel_size=2,stride=2))
    #the way using * has been seen before, it means this is a string of number, like an array.
    return nn.Sequential(*layers)

conv_arch = ((2, 64), (2, 128 ), (3, 256), (3, 512), (3, 512))

def vgg(conv_arch):
    conv_blks = []
    in_channels = 1
    # 卷积层部分
    for (num_convs, out_channels) in conv_arch:
        conv_blks.append(vgg_block(num_convs, in_channels, out_channels))
        in_channels = out_channels

    return nn.Sequential(
        *conv_blks, nn.Flatten(),
        # 全连接层部分
        nn.Linear(out_channels * 7 * 7, 4096), nn.ReLU(), nn.Dropout(0.5),
        nn.Linear(4096, 4096), nn.ReLU(), nn.Dropout(0.5),
        nn.Linear(4096, 10))

net = vgg(conv_arch)

#the first number in size is set for iters. You use train_iter to load a batch size, 
# then the first is just the size of the batch. 
X = torch.randn(size=(1, 1, 224, 224))
for blk in net:
    X = blk(X)
    print(blk.__class__.__name__, 'output shape:\t', X.shape)
#the channels is so large that the consumption of  this algorithm is not cheap

ratio = 4
small_conv_arch = [(pair[0], pair[1] // ratio) for pair in conv_arch]

net = vgg(small_conv_arch)

#when lr = 0.05, it has better performs. 
lr, num_epochs, batch_size = 0.05, 10, 128
#in the process of inference, it does not need more epochs.
train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size, resize=224)
d2l.train_ch6(net, train_iter, test_iter, num_epochs, lr, d2l.try_gpu())

net_save_path = os.path.join(net_save_dir, 'VGGnet.pt')
torch.save(net.state_dict(), net_save_path)

loss = nn.CrossEntropyLoss()
#inference
#@save
# def inferrence_ch6(net, train_iter, num_epochs, device):
#     """用GPU训练模型(在第六章定义)"""
#     '''def init_weights(m):
#         if type(m) == nn.Linear or type(m) == nn.Conv2d:
#             nn.init.xavier_uniform_(m.weight)
#     net.apply(init_weights)
#     '''

#     print('inferrencing on', device)
#     net.to(device)
#     '''optimizer = torch.optim.SGD(net.parameters(), lr=lr)
#     loss = nn.CrossEntropyLoss()
#     '''
#     animator = d2l.Animator(xlabel='epoch', xlim=[1, 30], legend=['train acc', 'train loss'])
#     timer, num_batches = d2l.Timer(), len(train_iter) 
    
#     #load the net parameters saved
#     print('***********parameters loading**************')
#     net_save_path = os.path.join(net_save_dir, 'VGGnet.pt')
#     if os.path.exists(net_save_path):
#         loaded_paras = torch.load(net_save_path)
#         net.load_state_dict(loaded_paras)
#         net.eval() # be ccautious about this

#     with torch.no_grad():
#         for epoch in range(num_epochs):
#             # 训练损失之和，训练准确率之和，样本数
#             metric = d2l.Accumulator(3)
#             net.train()
#             for i, (X, y) in enumerate(train_iter):
#                 timer.start()
#                 #optimizer.zero_grad()
#                 X, y = X.to(device), y.to(device)
#                 y_hat = net(X)
#                 import ipdb; ipdb.set_trace()
#                 l = loss(y_hat, y)
#                 #l.backward()
#                 #optimizer.step()
#                 #with torch.no_grad():
#                 metric.add(d2l.accuracy(y_hat, y), l*X.shape[0], X.shape[0])
#                 timer.stop()
#                 train_l = metric[1] / metric[2]
#                 train_acc = metric[0] / metric[2]
#                 #do not understand
#                 if (i + 1) % (num_batches // 20) == 0 or i == num_batches - 1:
#                     animator.add(epoch + (i + 1) / num_batches, (train_acc, train_l))
#                 '''if i  == 10 and (epoch == 20):
#                     text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat', 
#                                     'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
#                     for k, m in enumerate(y):
#                         print(f'labels:{k}, {text_labels[m]}\n')
#                     print('{y.shape[0]}\n')
#                 '''
#             #test_acc = evaluate_accuracy_gpu(net, test_iter)#used to draw curve
#             #animator.add(epoch + 1, (None, test_acc))
#     print(f'train acc {train_acc:.3f}\n, 'f'train loss {train_l:.3f}\n, ')
#     print(f'{metric[1] * num_epochs / timer.sum():.1f} examples/sec '
#           f'on {str(device)}')

# inferrence_ch6(net, train_iter, num_epochs, d2l.try_gpu())

d2l.plt.show()
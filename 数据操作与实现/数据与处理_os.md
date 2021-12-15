**One-hot-encode with pandas**  
```python
import os
import pandas as pd
#path = '~\下载\code_vs\covid_test.csv'
data = pd.read_csv(data_file)
print(data)
```
```python
inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs = inputs.fillna(inputs.mean())
print(inputs)
inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)
```
**intepretation**  

     get-dummies, this is a function to fulfill one_hot_encode  
     and one-hot-encoed just thinks all the varible characters as variable  characters and use 0001 to encode them

![pandas.one-hot](https://github.com/pipiyea287/ubuntu_git_file/blob/main/picture/one_hot_encode.png)  

   **I don't know why there are always some mistakes with relative paths to show the picture**
## linear algebra  
```python
sum_A = A.sum(axis=1, keepdims=True)
```
     1随着sum的操作，矩阵会降维，损失高纬度信息。为了保存高纬度信息，使用keepdims=True,然后维度还会保留，只是变为1，例如如果A是3*4的矩阵，这样之后就会变成1*4的矩阵。  
     2如此就可以进行广播操作，广播操作要求维度数量一致，不要求大小一致，广播会自动补全1.
     3***发现tab形成文字块对中英文tab有要求。应该是tab=4个空格（1个字符），中英文字符大小不一致。***

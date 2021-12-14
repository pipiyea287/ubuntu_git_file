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

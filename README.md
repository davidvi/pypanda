## pypanda
Python implementation of PANDA (Passing Attributes between Networks for Data Assimilation)  

_Glass K, Huttenhower C, Quackenbush J, Yuan GC. Passing Messages Between Biological Networks to Refine Predicted Interactions, PLoS One, 2013 May 31;8(5):e64832_

##### Table of Contents
[Panda algorithm](#panda)
[Installation](#installation)  
[Usage](#usage)  

##### Panda implementation
To find agreement between the three input networks first the responsibility (R) is calculated.
![Image](http://www.sciweavers.org/download/Tex2Img_1453458635.jpg)
Thereafter availability (A) is calculated.
![equation](http://latex.codecogs.com/gif.download?A_%7Bij%7D%5E%7B%28t%29%7D%3DT%28W_%7Bi.%7D%5E%7B%28t-1%29%7D%2C%20C_%7B.j%7D%5E%7B%28t-1%29%7D%29)


##### Installation
```no-highlight
git clone https://github.com/davidvi/pypanda.git
cd pypanda
sudo python setup.py install
```

##### Usage
```no-highlight
#import pypanda library
from pypanda import panda
from pypanda import lioness
import pandas as pd
#run panda
p = panda('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt', remove_missing=False)
#save results
p.save_panda_results(file = 'Toy_Panda.pairs')
#calculate indegree
indegree = p.return_panda_indegree()
print indegree.head()
#calculate outdegree
outdegree = p.return_panda_outdegree()
print outdegree.head()
#run lioness
l = lioness(p)
#save results
l.save_lioness_results(file = 'Toy_Lioness.txt')
```

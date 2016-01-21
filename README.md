## pypanda
Python implementation of PANDA (Passing Attributes between Networks for Data Assimilation)  

_Glass K, Huttenhower C, Quackenbush J, Yuan GC. Passing Messages Between Biological Networks to Refine Predicted Interactions, PLoS One, 2013 May 31;8(5):e64832_

##### Table of Contents
[Installation](#installation)  
[Usage](#usage)  

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

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
![Image](http://www.sciweavers.org/download/Tex2Img_1453459119.jpg)  
Availability and responsibility are combined with the following formula.  
![Image](http://www.sciweavers.org/download/Tex2Img_1453459183.jpg)  
Protein cooperativity and gene co-regulatory networks are updated.  
![Image](http://www.sciweavers.org/download/Tex2Img_1453459226.jpg)  
![Image](http://www.sciweavers.org/download/Tex2Img_1453459305.jpg)  
P and C are updated to satisfy convergence.  
![Image](http://www.sciweavers.org/download/Tex2Img_1453459359.jpg)  
![Image](http://www.sciweavers.org/download/Tex2Img_1453459389.jpg)  
Hamming distance is calculated every iteration.
![Image](http://www.sciweavers.org/download/Tex2Img_1453459429.jpg)  


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

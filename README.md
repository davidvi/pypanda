## PyPanda (Python Panda)
Python implementation of PANDA (Passing Attributes between Networks for Data Assimilation)  

_Glass K, Huttenhower C, Quackenbush J, Yuan GC. Passing Messages Between Biological Networks to Refine Predicted Interactions, PLoS One, 2013 May 31;8(5):e64832_

### Table of Contents
* [Panda implementation](#panda-implementation)  
* [Installation](#installation)  
* [Usage](#usage)  
  * [iPython](#run-from-ipython-notebook)  
  * [Terminal](#run-from-the-terminal)  

### Panda implementation
To find agreement between the three input networks first the responsibility (R) is calculated.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/responsibility.png" height="30">  

Thereafter availability (A) is calculated.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/availability.png" height="30">  

Availability and responsibility are combined with the following formula.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/combine.png" height="30">  

Protein cooperativity and gene co-regulatory networks are updated.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/cooperativity.png" height="30">  
<img src="https://github.com/davidvi/pypanda/raw/develop/img/co-regulatory.png" height="30">  

P and C are updated to satisfy convergence.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/p.png" height="30">  
<img src="https://github.com/davidvi/pypanda/raw/develop/img/c.png" height="30">  

Hamming distance is calculated every iteration.  

<img src="https://github.com/davidvi/pypanda/raw/develop/img/hamming.png" height="40">  


### Installation
```no-highlight
git clone https://github.com/davidvi/pypanda.git
cd pypanda
sudo python setup.py install
```

### Usage
#### Run from iPython notebook
Import PyPanda library:
```python
from pypanda import panda
from pypanda import lioness
import pandas as pd
```
Run Panda algorithm:
```python
p = panda('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt', remove_missing=False)
```
Save the results:
```python
p.save_panda_results(file = 'Toy_Panda.pairs')
```
Calculate indegrees for further analysis:
```python
indegree = p.return_panda_indegree()
```
Calculate outdegrees for further analysis:
```python
outdegree = p.return_panda_outdegree()
```
Run the Lioness algorithm for single sample networks:
```python
l = lioness(p)
```
Save Lioness results:
```python
l.save_lioness_results(file = 'Toy_Lioness.txt')
```
#### Run from the terminal

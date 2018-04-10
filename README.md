## Fork description
I corrected the code after some methods have been deprecated. I added the import for AnalyzePanda and AnalyzeLioness in this README. 


## PyPanda (Python Panda)
Python implementation of PANDA (Passing Attributes between Networks for Data Assimilation)  

_Glass K, Huttenhower C, Quackenbush J, Yuan GC. Passing Messages Between Biological Networks to Refine Predicted Interactions, PLoS One, 2013 May 31;8(5):e64832_

### Table of Contents
* [Panda implementation](#panda-algorithm)  
* [Installation](#installation)  
* [Usage](#usage)  
  * [iPython](#run-from-ipython-notebook)  
  * [Terminal](#run-from-the-terminal)  
* [Results] (#results)

### Panda algorithm
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
PyPanda requires Python 2.7. We recommand the following commands to install PyPanda (on Ubuntu and Debian derived systems, also works on OSX):
#### With root access
```no-highlight
git clone https://github.com/davidvi/pypanda.git
cd pypanda
sudo python setup.py install
```
#### Without root access
```no-highlight
git clone https://github.com/davidvi/pypanda.git
cd pypanda
python setup.py install --user
#to run from the command line you will need to make pypanda executable and add the bin directory to your PATH:
cd bin
chmod +x pypanda
echo "$(pwd):PATH" >> ~/.bashrc
source ~/.bashrc
```
To run PyPanda from Windows (tested on Windows 10) install Git (https://git-scm.com/downloads) and Anaconda Python2.7 (https://www.continuum.io/downloads) and from the Anaconda Prompt run:
```no-highlight
git clone https://github.com/davidvi/pypanda.git
cd pypanda
python setup.py install
```
### Usage
#### Run from the terminal
PyPanda can be run directly from the terminal with the following options:
```
-h help
-e (required) expression values
-m (optional) pair file of motif edges, when not provided analysis continues with Pearson correlation matrix
-p (optional) pair file of PPI edges
-f (optional) remove missing values (default is False)
-o (required) output file
-q (optional) output lioness single sample network
```
To run PyPanda on the example data:
```
$ pypanda -e ToyData/ToyExpressionData.txt -m ToyData/ToyMotifData.txt -p ToyData/ToyPPIData.txt -f True -o test_panda.txt -q test_lioness.txt
```
To reconstruct a single sample Lioness Pearson correlation network:
```
$ pypanda -e ToyData/ToyExpressionData.txt -o test_panda_pearson.txt -q test_lioness_pearson.txt
```
#### Run from iPython notebook
Import PyPanda library:
```python
from pypanda import Panda
from pypanda import Lioness
import pandas as pd
from pypanda.analyze_panda import AnalyzePanda
from pypanda.analyze_lioness import AnalyzeLioness
```
Run Panda algorithm, leave out motif and PPI data to use Pearson correlation network:
```python
p = Panda('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt', remove_missing=False)
```
Save the results:
```python
p.save_panda_results(file = 'Toy_Panda.pairs')
```
Return a network plot:
```python
plot = AnalyzePanda(p)
plot.top_network_plot(top=100, file='top_100_genes.png')
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
l = Lioness(p)
```
Save Lioness results:
```python
l.save_lioness_results(file = 'Toy_Lioness.txt')
```
Return a network plot for one of the Lioness single sample networks:
```python
plot = AnalyzeLioness(l)
plot.top_network_plot(column= 0, top=100, file='top_100_genes.png')
```
### Results
```
Example Panda output:
TF  Gene  Motif Force
---------------------
CEBPA	AACSL	0.0	-0.951416589143
CREB1	AACSL	0.0	-0.904241609324
DDIT3	AACSL	0.0	-0.956471642313
E2F1	AACSL	1.0	3.6853160511
EGR1	AACSL	0.0	-0.695698519643

Example lioness output:
Sample1 Sample2 Sample3 Sample4
-------------------------------
-0.667452814003	-1.70433776179	-0.158129613892	-0.655795512803
-0.843366539284	-0.733709815256	-0.84849895139	-0.915217389738
3.23445386464	2.68888472802	3.35809757371	3.05297381396
2.39500370135	1.84608635425	2.80179804094	2.67540878165
-0.117475863987	0.494923925853	0.0518448588965	-0.0584810456421

TF, Gene and Motif order is identical to the panda output file.
```

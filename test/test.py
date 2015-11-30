from pypanda import panda
from pypanda import lioness
import pandas as pd

#run panda
p = panda('../ToyData/ToyExpressionData.txt', '../ToyData/ToyMotifData.txt', '../ToyData/ToyPPIData.txt', remove_missing=False)
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

from pypanda import Panda
from pypanda import Lioness
import pandas as pd

#run panda
p = Panda('../ToyData/ToyExpressionData.txt', '../ToyData/ToyMotifData.txt', '../ToyData/ToyPPIData.txt', remove_missing=False)
#p = panda('normalized_short_processed_data_names.txt', 'normalized_short_motif.txt', 'normalized_short_protein.txt', remove_missing=True)
#save results
p.save_panda_results(file = 'toy_Panda.pairs')
#calculate indegree
indegree = p.return_panda_indegree()
print indegree.head()
#calculate outdegree
outdegree = p.return_panda_outdegree()
print outdegree.head()
#run lioness
l = Lioness(p)
#save results
l.save_lioness_results(file = 'toy_Lioness.txt')

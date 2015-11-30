from pypanda import panda
from pypanda import lioness
import time

total_run_time = time.time()

#p = panda('../../data/raw/eh_1000_before_shape.txt', '../../data/reference/motifprior_CISBP.txt', '../../data/reference/PPI_CISBP.txt', remove_missing=True)
#p = panda('../../data/normalized/normalized_short_processed_data_names.txt', '../../data/normalized/normalized_short_motif.txt', '../../data/normalized/normalized_short_protein.txt')
p = panda('../../data/normalized/ToyExpressionData.txt', '../../data/normalized/ToyMotifData.txt', '../../data/normalized/ToyPPIData.txt', remove_missing=False)
#print p.panda_network
p.save_panda_results(file = 'short.pairs')
#r.lioness()
#print r.lioness_network
#l = lioness(p)
#l.save_lioness_results()
#print l.lioness_network
#l.save_lioness_results()
print p.return_panda_indegree()
print p.return_panda_outdegree()
print('total running time: %s seconds' % (time.time() - total_run_time))

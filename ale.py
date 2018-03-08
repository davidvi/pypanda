from __future__ import print_function

import pandas as pd
import numpy as np

import functools
import time
import math
from pypanda import Panda
from pypanda import Lioness
import pandas as pd
from pypanda.analyze_panda import AnalyzePanda
from pypanda.analyze_lioness import AnalyzeLioness
def main(argv):

    p = Panda('ToyData/ToyExpressionData.txt', 'ToyData/ToyMotifData.txt', 'ToyData/ToyPPIData.txt', remove_missing=False)

    p.save_panda_results(file = 'Toy_Panda.pairs')
    plot = AnalyzePanda(p)
    plot.top_network_plot(top=100, file='top_100_genes.png')

if __name__ == '__main__':
    main()
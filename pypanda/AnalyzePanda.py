from __future__ import print_function

from pypanda import Panda

import numpy as np
import pandas as pd
import networkx as nx

class AnalyzePanda(panda):
    '''Network plot.'''
    def __init__(self, panda_data):
        '''Load variables from panda.'''
        self.panda_results = panda_data.export_panda_results
        return None
    def top_network_plot(self, top = 100):
        '''Create network plot for top genes.'''

        return None
    def __shape_plot_network():

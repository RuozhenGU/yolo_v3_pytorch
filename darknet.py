from __future__ import division
import torch
import torch.nn
import torch.nn.functional
from torch.autograd import Variable
import numpy as np

def parse_cfg(cfg_file):
    """
    Pase the cfg file and returns lst of dicts/blocks describing the nn layer
    """

    cfg_file = open(cfg_file, 'r')
    lines = file.read().split('\n')

    # get rid of comments
    lines = [x for x in lines if x[0] != '#']
    # get rid of empty lines
    lines = [x for x in lines if not len(x))]
    # get rid of whitespaces
    lines = [x.rstrip().lstrip() for x in lines]

    # store block data
    
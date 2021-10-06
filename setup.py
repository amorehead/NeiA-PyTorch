#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='NeiA-PyTorch',
    version='1.0.0',
    description='An open-source PyTorch implementation of the Neighborhood Averaging (NeiA) GNN layer.',
    author='Alex Morehead',
    author_email='alex.morehead@gmail.com',
    url='https://github.com/amorehead/NeiA-PyTorch',
    install_requires=[
        'setuptools==57.4.0',
        'dill==0.3.4',
        'tqdm==4.62.0',
        'torchmetrics==0.5.1',
        'wandb==0.12.2',
        'pytorch-lightning==1.4.8',
        'fairscale==0.4.0'
    ],
    packages=find_packages(),
)

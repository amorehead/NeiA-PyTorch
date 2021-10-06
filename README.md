# NeiA-PyTorch
An open-source PyTorch implementation of the Neighborhood Averaging (NeiA) GNN layer.

## Citing this work

If you use the code associated with this package, please cite:

```bibtex
@misc{morehead2021dipsplus,
      title={DIPS-Plus: The Enhanced Database of Interacting Protein Structures for Interface Prediction}, 
      author={Alex Morehead and Chen Chen and Ada Sedova and Jianlin Cheng},
      year={2021},
      eprint={2106.04362},
      archivePrefix={arXiv},
      primaryClass={q-bio.QM}
}
```

In addition, please cite the original authors of NeiA/NeiWA:

```bibtext
@inproceedings{liu2020deep,
  title={Deep learning of high-order interactions for protein interface prediction},
  author={Liu, Yi and Yuan, Hao and Cai, Lei and Ji, Shuiwang},
  booktitle={Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages={679--687},
  year={2020}
}
```

## Installation

First, install and configure Conda environment:

```bash
# Clone this repository:
git clone https://github.com/amorehead/NeiA-PyTorch

# Change to project directory:
cd NeiA-PyTorch

# Set up Conda environment locally
conda env create --name NeiA-PyTorch -f environment.yml

# Activate Conda environment located in the current directory:
conda activate NeiA-PyTorch

# (Optional) Perform a full install of the pip dependencies described in 'requirements.txt':
pip3 install -r requirements.txt

# (Optional) To remove the long Conda environment prefix in your shell prompt, modify the env_prompt setting in your .condarc file with:
conda config --set env_prompt '({name})'
 ```

## Training

 ```bash
# Hint: Run `python3 lit_model_train.py --help` to see all available CLI arguments
cd project
python3 lit_model_train.py --lr 1e-3 --weight_decay 1e-2
cd ..
```
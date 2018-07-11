# OpenCog Unsupervised Language Learning project

## Dependencies
* Anaconda 3
* Numpy
* Pandas
* Scikit-Learn
* Jupyter notebook
* Matplotlib
* Cython
* SparseSVD
* PyTest

## Create virtual environment
```
conda env create -f environment.yml
```
## Run tests
```
cd ~/language-learning
source activate ull3
pytest
```
## Run Jupyter
```
cd ~/language-learning/notebooks
source activate ull3
jupyter notebook
```

## Grammar Tester Installation

From `language-learning` directory run:

```
source activate ull3
pip install .
```
If for some reason you are not using virtual environment or using Python 2.x along with Python 3.x make sure you 
run `pip3` instead:
```
pip3 install .
```

`opencog-ull` package will be installed to your virtual environment.
Command line scripts from `src/cli-scripts` are copied to `/bin` subdirectory in your virtual environment.

To uninstall the package type:
```
pip uninstall opencog-ull
```
If you are going to use grammar tester from within your own code see `src/samples` for use cases.


---

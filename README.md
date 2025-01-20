## 
     ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄       ▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄ 
    ▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░▌     ▐░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌░▌   ▐░▐░▌▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌
    ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌
    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌
    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
    ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌   ▀   ▐░▌▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
    ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌▐░▌          
    ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░▌       ▐░▌▐░▌     ▐░▐░▌▐░▌          
    ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌       ▐░▌▐░▌      ▐░░▌▐░▌          
     ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀         ▀  ▀        ▀▀  ▀           



# EnMNP: A Deep Learning predictor for MHC-I (Neo)epitope Prediction

EnMNP (Ensembled Multi-Factor Neoepitope Predictor) is a state-of-the-art machine learning-based neoepitope predictor for predicting the presentation of MHC-I (neo)epitopes and evaluating their immunogenicity. By leveraging transfer learning and creating an architecture that combines a powerful self-attention mechanism-based core model on protein sequences with an ensemble of diverse weak learners focused on various neoepitope-related characteristics, EnMNP achieves enhanced predictive accuracy and sensitivity for neoepitope prediction.

By utilizing advanced neural network models, EnMNP facilitates research on immune responses and contributes to the development of innovative immunotherapies.

Below is the list of software dependencies used during testing.

### Required Dependencies

| Dependency | Version |
|------------|---------|
| [python](https://www.python.org) | 3.9.13 |
| [numpy](https://numpy.org) | 1.21.5 |
| [pytorch](https://pytorch.org) | 1.13.0 |
| [pandas](https://pandas.pydata.org) | 1.4.4 |
| [psutil](https://pypi.org/project/psutil) | 5.9.4 |

### Optional Dependencies

| Dependency | Version | Description |
|------------|---------|-------------|
| [cuda](https://developer.nvidia.com/cuda-downloads) | 11.7 | Required for GPU acceleration |
| [magma](https://developer.nvidia.com/magma) | magma-cuda117 version 2.6.1 | Recommended for GPU usage |

### Jupyter Notebook Dependencies

| Dependency | Version |
|------------|---------|
| [scipy](https://scipy.org/) | 1.7.3 |
| [scikit-learn](https://scikit-learn.org) | 1.0.2 |
| [matplotlib](https://matplotlib.org/) | 3.5.3 |
| [seaborn](https://seaborn.pydata.org/) | 0.12.1 |
| [py3dmol](https://pypi.org/project/py3Dmol/) | 2.0.0.post2 |
| [logomaker](https://pypi.org/project/logomaker/) | 0.8 |
| [openpyxl](https://pypi.org/project/openpyxl) | 3.1.1 |

## Usage

EnMNP provides two main executable Python scripts located in the `src` directory: `predict.py` and `train.py`.

| Script        | Description |
|---------------|-------------|
| `predict.py`  | Used for making predictions using EnMNP EL and EnMNP IM models |
| `train.py`    | Allows users to train or retrain models (via transfer learning) on new data |

Both scripts can be executed from any directory and offer helpful usage text.
* `python predict.py --help`
* `python train.py --help`

### Supported Alleles

EnMNP supports MHC-I allele predictions only. The tool uses fuzzy string matching to map various MHC allele naming conventions to standardized names. For example, `HLA-A*02:01`, `A*02:01`, `HLAA0201`, and `A0201` are all interpreted as equivalent. Synonymous substitutions and noncoding fields (e.g., `HLA-A*02:01:01`) are also properly handled.

**Note:** EnMNP does not validate allele names. Predictions will be made even if invalid or MHC-II alleles are provided, with the tool matching them to the closest valid MHC-I allele.

The list of alleles used in the multiple sequence alignment is available in the [pseudosequences data file](data/pseudoseqs.csv).

### Required Arguments

| Argument | Description |
|----------|-------------|
| `-i` or `--input` | CSV file containing peptide sequences (column indices are zero-based). Must include a column of peptides and optionally, MHC-I allele names. |
| `-m` or `--model` | Specifies which EnMNP model to use for predictions: <br> `el` or `enmnp_el` for EnMNP EL <br> `im` or `enmnp_im` for EnMNP IM <br> Directory path to a custom model (for retraining with `train.py`). |

### Arguments for Training Models

| Argument | Description |
|----------|-------------|
| `-t` or `--tgtcol` | Index of the column containing target (ground truth) values. |
| `-o` or `--out` | Directory where model parameters will be saved for each training epoch. Optional during transfer learning, defaults to the base model directory. |

### Input Formatting

| Argument | Description |
|----------|-------------|
| `-a` or `--allele` | Column index or specific allele name for MHC-I prediction. If provided as a column, each row must contain a single MHC-I allele. |
| `-p` or `--pepcol` | Column index where peptide sequences are located in the input CSV. |
| `-c` or `--hdrcnt` | The number of header rows to skip before processing data in the input CSV file. |

### Output Options

| Argument | Description |
|----------|-------------|
| `-o` or `--out` | Specifies the output file or directory for saving results: <br> For `predict.py`, results are saved to `input.prd` by default. <br> For `train.py`, retrained models are saved to the specified directory (defaults to the base model directory during transfer learning). |
| `-z` or `--saveatt` | Option to save attention values for `predict.py`. Set to `1` to save, `0` to exclude. |

### Other Optional Arguments

| Argument | Description |
|----------|-------------|
| `-d` or `--devices` | Specify the devices for running EnMNP. Options include: <br> `all` to use all GPUs <br> Comma-separated list of GPU indices to use a subset of GPUs <br> `cpu` to run on the CPU (not recommended for large datasets) |
| `-v` or `--verbose` | Enable verbose logging. Set to `1` for true, `0` for false. |
| `-j` or `--jobs` | Specify the number of parallel workers to load data. |
| `-f` or `--prefetch` | Set the number of batches to prefetch per worker. |
| `-b` or `--maxbat` | Set the maximum batch size (reduce if memory issues occur). For `predict.py`, the default maximizes GPU usage with minimal memory consumption. |
| `-s` or `--pseudoseqs` | Provide a CSV mapping MHC-I alleles to their one-hot encoded representation. |
| `-l` or `--lr` | Set the learning rate for the AdamW optimizer (only for `train.py`). |
| `-e` or `--epochs` | Specify the number of epochs for training (only for `train.py`). |


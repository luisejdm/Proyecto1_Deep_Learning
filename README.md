# Proyecto1_Deep_Learning

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

Proyecto 1 - Deep Learning

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- The final, canonical data sets for modeling
│   │   ├── x_test_128.npy
│   │   ├── x_test_full.npy
│   │   ├── x_test.npy
│   │   ├── x_train_128.npy
│   │   ├── x_train_full.npy
│   │   └── x_train.npy
│   └── raw            <- The original, immutable data dump
│       └── Motorbikes/
│
├── docs               <- Project documentation (mkdocs)
│   ├── mkdocs.yml
│   ├── README.md
│   └── docs/
│       ├── getting-started.md
│       ├── index.md
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│   ├── decoder_lejdm_3_07.keras
│   ├── decoder_smdo_3-04.keras
│   ├── decoder_smdo_3-05.keras
│   ├── decoder_src_3_06.keras
│   ├── encoder_lejdm_3_07.keras
│   ├── encoder_smdo_3-04.keras
│   ├── encoder_smdo_3-05.keras
│   ├── encoder_src_3_06.keras
│   ├── vae_model.keras
│   └── vae_smdo_3-04.keras
│
├── notebooks          <- Jupyter notebooks. Naming convention: number, creator's initials, and short description
│   ├── 0.01-src-initial-data-exp.ipynb
│   ├── 1.01-lejdm-data-preprocessing.ipynb
│   ├── 1.02-smdo-data_preprocessing_dif_size_128.ipynb
│   ├── 1.03-src-data-preprocessing.ipynb
│   ├── 2.01-lejdm-data-visualization.ipynb
│   ├── 3.01-lejdm-first-vae.ipynb
│   ├── 3.02-smdo-first_vae_attempts.ipynb
│   ├── 3.03-src-vae-exploration.ipynb
│   ├── 3.04-smdo-first_vae_refining.ipynb
│   ├── 3.05-smdo-refining_further.ipynb
│   ├── 3.06-src-exploring_tato_vae.ipynb
│   └── 3.07-lejdm-refining_further_v2.ipynb
│
├── pyproject.toml     <- Project configuration file with package metadata and tool configuration
│
├── references         <- Data dictionaries, manuals, and other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment
│
└── proyecto1_deep_learning   <- Source code for use in this project
    ├── __init__.py             <- Makes proyecto1_deep_learning a Python module
    ├── data_loader.py          <- Data loading utilities
    ├── config.py               <- Store useful variables and configuration
    ├── dataset.py              <- Scripts to download or generate data
    ├── features.py             <- Code to create features for modeling
    ├── modeling                <- Model training and inference
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models
    │   └── train.py            <- Code to train models
    └── plots.py                <- Code to create visualizations
```

--------


# Plot Figure Scripts
This repository contains scripts for generating figures for our research project. The scripts visualize data from the `data` folder and save the resulting images to the `imgs` folder.

## Figures Included

This repository includes scripts for generating the following figures:
- Figures 1-3
- Figures 8-18

## Setup and Usage

Follow these steps to generate the figures:

1. Clone the SMORE repository:

```bash
git clone https://github.com/arctanln2/smore.git
```

2. Navigate to the plot_figure directory:

```bash
cd smore/plot_figure
```
3. Create the output directory for images:

```bash
mkdir imgs
```
4. Run the desired plotting script, for example:

```bash
python scripts/plot_fig1.py
```

## Directory Structure
```bash
plot_figure/
├── scripts/         # Contains all plotting scripts
│   ├── plot_fig1.py
│   └── ...
├── data/            # Contains data files used by the scripts
│   ├── dataset1.csv
│   └── ...
├── imgs/            # Generated figures will be saved here
└── README.md
```

## Available Scripts
### Figures 1-3

```bash
python scripts/plot_fig1.py
python scripts/plot_fig2.py
python scripts/plot_fig3.py
```
### Figures 8-18

```bash
python scripts/plot_fig8.py
# ... and so on through
python scripts/plot_fig18.py
```
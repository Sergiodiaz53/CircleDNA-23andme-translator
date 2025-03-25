# Genetic Data File Converter

## Overview

This Python script converts genetic data files from Circle format to a 23andMe-like format. It provides a simple command-line tool to transform genetic data files by restructuring columns and formatting.

## Features

- Convert genetic data files with a single command
- Supports custom input and output file paths
- Robust error handling
- Simple and straightforward data transformation

## Prerequisites

- Python 3.7+
- No external dependencies required

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/genetic-data-converter.git
   cd genetic-data-converter
   ```

2. Ensure you have Python installed (3.7 or later recommended)

## Usage

### Basic Usage

```bash
python genetic_data_converter.py -i input_file
```

This will create an `output.txt` file in the current directory.

### Specify Input and Output Files

```bash
python genetic_data_converter.py -i input_file -o custom_output.txt
```

### Command-Line Arguments

- `-i` or `--input`: **Required**. Path to the input genetic data file
- `-o` or `--output`: **Optional**. Path for the output file (default: `output.txt`)

## Input File Format

Expected input file format:
- Tab-separated values
- Columns: 
  1. Marker Name (rsid)
  2. Chromosome 
  3. Position
  4. Genotype

Example input:
```
MarkerName    chr1    12345    A/G
```

## Output File Format

The script converts to:
- Tab-separated values
- Columns:
  1. rsid
  2. Chromosome (chr prefix removed)
  3. Position
  4. Genotype (slashes removed)

Example output:
```
rsid    1    12345    AG
```
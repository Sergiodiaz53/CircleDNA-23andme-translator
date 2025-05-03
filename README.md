# CircleDNA-23andme translator

## Overview

This Python script converts genetic data files from Circle format to a 23andMe-like format. It provides a simple command-line tool to transform genetic data files by restructuring columns and formatting.
This will allow you to use pages like genomelink.io, geneticgenie.org, selfdecode.com, geneticlifehacks.com...

In order to get your CircleDNA raw data, you have to write an email to care[at]circledna.com with your information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sergiodiaz53/CircleDNA-23andme-translator.git
   cd CircleDNA-23andme-translator
   ```

2. Ensure you have Python installed (Tested in Python 3.11.9)

## Usage

### Basic Usage

```bash
python translator.py -i input_file
```

This will create an `output.txt` file in the current directory.

### Specify Input and Output Files

```bash
python translator.py -i input_file -o custom_output.txt
```

### Enable Reduced Mode with RSID Filtering

To filter the output file so it only contains lines where the `markername` (rsid) is present in a provided RSID list file:

```bash
python translator.py -i input_file -o custom_output.txt --reduced --rsid-file rsid-list.txt
```

- `--reduced`: Enables reduced mode to filter the output based on an RSID list.
- `--rsid-file`: Path to the RSID list file.

This allows you to reduce the file size of the original CircleDNA data by selecting only specific RSIDs. The current rsid-list.txt is based on the data used by Geneticlifehacks.com. Thanks to [Debbie Moon](https://www.geneticlifehacks.com/about/) for providing it.

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
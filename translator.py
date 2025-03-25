import os
import argparse
import sys

def validate_input_files(input_file, output_file):
    """
    Validate input and output file paths before processing.
    
    Args:
        input_file (str): Path to the Circle input file
        output_file (str): Path to the 23andme output-like file
    
    Raises:
        FileNotFoundError: If input file does not exist
        PermissionError: If output file cannot be written
    """
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
    
    try:
        with open(output_file, 'w') as _:
            pass
    except PermissionError:
        raise PermissionError(f"Cannot write to output file '{output_file}'")

def convert_genetic_data(input_file, output_file):
    """
    Convert genetic data file from one format to another.
    
    Args:
        input_file (str): Path to the input genetic data file
        output_file (str): Path to the output converted file
    """
    validate_input_files(input_file, output_file)
    
    try:
        with open(input_file, "r") as infile, open(output_file, "w") as outfile:
            # Read the header line from the input file
            header = infile.readline().strip().split("\t")
            
            # Write the new header to the output file
            outfile.write("rsid\tchromosome\tposition\tgenotype\n")
            
            # Process each line in the input file
            for line_number, line in enumerate(infile, start=2):
                try:
                    # Split the line into columns
                    columns = line.strip().split("\t")
                    
                    # Validate input data
                    if len(columns) < 4:
                        print(f"Warning: Insufficient columns in line {line_number}")
                        continue
                    
                    # Extract the relevant information and transform it
                    markername = columns[0]  # rsid
                    chrom = columns[1].replace("chr", "")  # Remove "chr" prefix
                    pos = columns[2]  # position
                    gt = columns[3].replace("/", "")  # Replace "/" with "" for genotype
                    
                    # Write the transformed data to the output file
                    outfile.write(f"{markername}\t{chrom}\t{pos}\t{gt}\n")
                
                except Exception as line_error:
                    print(f"Error processing line {line_number}: {line_error}")
    
    except IOError as file_error:
        print(f"File processing error: {file_error}")
    
    print(f"File has been converted and saved as '{output_file}'")

def main():
    parser = argparse.ArgumentParser(description='Convert genetic data file format.')
    parser.add_argument('-i', '--input', 
                        required=True, 
                        help='Path to the Circle genetic data input file')
    parser.add_argument('-o', '--output', 
                        default='output.txt', 
                        help='Path to the 23andme output-like converted file (default: output.txt)')
    
    args = parser.parse_args()
    
    try:
        convert_genetic_data(args.input, args.output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
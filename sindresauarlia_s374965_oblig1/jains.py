import sys

"""
This program calculates Jain's Fairness index for a given list of throughput values.
To run the program, use the following command:
python3 jains.py <file_name>"
"""

def calculate_jfi(throughput: list[int]):
    """
    Calculates Jain's Fairness index for a given list of throughput values.
    """
    print(f"Throughput values: {throughput}")
    # Explanation of the formula: the sum of the throughput values squared divided by the number of values, divided by the sum of the squared values.
    numerator = sum(throughput) ** 2
    denominator = len(throughput) * sum([x ** 2 for x in throughput])
    jfi = numerator / denominator
    return jfi


def convert_to_kbps(value: str):
    """
    Converts all throughput value to Kbps.
    """
    number, unit = value.split()
    number = float(number)
    if unit == "Mbps":
        return number * 1000  # Convert Mbps to Kbps
    elif unit == "Kbps":
        return number
    else:
        raise ValueError("Invalid unit. Only Mbps and Kbps are supported.")

def main():
    '''
    The main function of the program. It takes a file name as an argument, reads the throughput values from the file, and calculates Jain's Fairness index.
    '''
    # Check if a file name is provided
    if len(sys.argv) < 2:
        print("No input provided. Please provide a file name.")
        return

    # Read the throughput values from the file and calculate Jain's Fairness index
    try:
        with open(sys.argv[1], 'r') as file:
            throughput = [convert_to_kbps(line.strip()) for line in file]
        jfi = calculate_jfi(throughput) # Calculate Jain's Fairness index
        print(f"Jain's Fairness index is: {jfi:.4f}") # Print the result with 4 decimal places

    # Handle exceptions if the file contains invalid values
    except (ValueError, SyntaxError, FileNotFoundError):
        print("Invalid input. Please provide a valid file name.")

if __name__ == "__main__":
    main()
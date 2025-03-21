import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Generate math problems')
    parser.add_argument("-n", type=int, help="Number of problems")
    parser.add_argument("-r", type=int, required=True, help="Value range")
    parser.add_argument("-e", help="Exercise file")
    parser.add_argument("-a", help="Answer file")
    return parser.parse_args()
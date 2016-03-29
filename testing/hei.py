import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--data", help="Path to data", required=True, nargs='*')
parser.add_argument("-o", "--output")
parser.add_argument("-p", "--p-value")

args = parser.parse_args()

print ("Data: ", args.data)
print ("O: ", args.output)
print ("P:", args.p_value)
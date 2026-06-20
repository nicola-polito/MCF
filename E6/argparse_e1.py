import argparse

parser=argparse.ArgumentParser(description= "calculate x to the power of y")
group=parser.add_mutually_exclusive_group()
parser.add_argument("x", help ="the base", type= int)
parser.add_argument("y",type=int, help="the exponent")
group.add_argument("-v", "--verbose", action = "store_true", default=0, help=" increase output verbosity")
group.add_argument("-q", "--quiet", action="store_true")
args=parser.parse_args()
answer= args.x**args.y
if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
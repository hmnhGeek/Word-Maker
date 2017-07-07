import wordmaker as mw
import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument('--all', action = 'store_true', help = 'Find all possible words')
parser.add_argument('--comp', action = 'store_true', help = 'Find all complementary words')
parser.add_argument('--len', action = 'store_true', help = 'Find all possible words of a given length')
parser.add_argument('alphabets', type = str, help = 'Find all possible words')
parser.add_argument('integer', type = int, help = 'Find all possible words')

args = parser.parse_args()

if args.all:
    
    mw.prettify(mw.makewords(args.alphabets, args.integer))

elif args.comp:
    mw.prettify(mw.complementary(args.alphabets, args.integer))

elif args.len:
    mw.prettify(mw.wordoflength(args.alphabets, args.integer))

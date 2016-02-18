import sys

def main():
    # returns a list of tuples of (rank, suit)
    lines = sys.stdin.readlines()
    rank_counts = [0 for i in range(10)]
    for line in lines:
        parts = line.split(',')
        rank = int(parts[-1])
        rank_counts[rank] += 1
    
    ranks = ["nothing", "one pair", "two pairs", "three of a kind", "a straight", "a flush", "a full house", "four of a kind", "a straight flush", "a royal flush"]
    for i in range(len(rank_counts)):
        print("The probability of {} is {:.4f}%".format(ranks[i], (100*float(rank_counts[i])/float(len(lines)))))

if __name__ == '__main__':
    main()

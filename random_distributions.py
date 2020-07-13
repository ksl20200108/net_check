import random

def transaction_fee():
    return random.uniform(0.1, 0.6)

def pdf_distribution():
    pass    # open and store txt

def main():
    print("the random number is %f" % transaction_fee())

main()

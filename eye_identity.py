# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

if __name__ == '__main__':
    n, m = map(int, raw_input().strip().split())
    numpy.set_printoptions(sign=' ')
    print(numpy.eye(n,m))

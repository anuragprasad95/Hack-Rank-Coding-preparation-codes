# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy

if __name__ == '__main__':
    input_number=tuple(map(int,raw_input().strip().split()))
    print numpy.zeros(input_number, dtype = numpy.int)
    print numpy.ones(input_number, dtype = numpy.int)

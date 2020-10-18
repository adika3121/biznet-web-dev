import numpy
def primesfrom3to(n):
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1



angka = int(input('Masukan Bilangan :'))
type(angka)
print(primesfrom3to(angka))
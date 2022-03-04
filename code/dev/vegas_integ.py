import vegas
import lhapdf

p = lhapdf.mkPDF("NNPDF31_lo_as_0118", 0)
mu = 91.188

def f(a):
    return lambda x: (p.xfxQ(1, x[0], mu) - p.xfxQ(-1, x[0], mu) ) / (x[0]) + a


integ = vegas.Integrator([[0, 1]])

result = integ(f(2), nitn=100, neval=10000)
print(result.summary())
print('result = %s    Q = %.2f' % (result, result.Q))
import numpy as np

data = [15, 16, 18, 19, 22, 24, 29, 30, 34]

print("mean:", np.mean(data))
print("median:", np.median(data))
print("50th percentile (median):", np.percentile(data, 50))
print("25th percentile:", np.percentile(data, 25))
print("75th percentile:", np.percentile(data, 75))
print("standard deviation:", np.std(data))
print("variance:", np.var(data))


# https://www.sololearn.com/learning/1094/2984/7251/1
# https://www.investopedia.com/ask/answers/021215/what-difference-between-standard-deviation-and-variance.asp
# https://www.mathsisfun.com/data/standard-deviation.html
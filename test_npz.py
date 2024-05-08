from numpy import load

data = load('case0005_slice000.npz')
lst = data.files
for item in lst:
    print(item)
    print(data[item])
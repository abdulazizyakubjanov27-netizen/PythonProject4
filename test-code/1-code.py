modules = ['requests']

for m in modules:
    mod = __import__(m)
    print(f"{m} version: {mod.__version__}")
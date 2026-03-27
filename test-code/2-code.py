# test_requests.py
modules = ['requests']  # Hozir faqat requests kerak

for m in modules:
    try:
        mod = __import__(m)           # Modulni import qilamiz
        print(f"{m} version: {mod.__version__}")  # Versiyasini chiqaramiz
    except ModuleNotFoundError:
        print(f"{m} modul o'rnatilmagan")
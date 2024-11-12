disk = 1.44 * 1024 * 1024


num = 100
lines = 50
chars = 25
bytes = 4

total_chars = num * lines * chars

total_bytes = total_chars * bytes

books = disk // total_bytes
print("Количество книг, помещающихся на дискету:", round(books))

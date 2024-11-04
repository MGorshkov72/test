weight_of_book_bayt = 25*50*100*4
weight_of_book_mb = weight_of_book_bayt / 1024 / 1024
num_book = round(1.44 // weight_of_book_mb)

print("Количество книг, помещающихся на дискету:", num_book)

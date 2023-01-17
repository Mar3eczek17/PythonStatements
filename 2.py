st = 'Print only the words that start with s in this sentence'

for i in st.split():
    if len(i) %2 == 0:
        print("even!")

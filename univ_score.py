school_number = input('何人測定しますか:')
standard_line = input('合格点は何点ですか:')
for i in range(int(school_number)):
    count = 0
    test_score = input('点数は何点でしたか:')
    how_many_absent = input('何回欠席しましたか:')
    absent_class = int(how_many_absent)*5
    your_score = int(test_score) - int(absent_class)
    print(your_score)
    count += 1
    if int(your_score) >= 25:
        print(count)

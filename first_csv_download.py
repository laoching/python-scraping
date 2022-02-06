import csv

csvFile = open('text.csv', 'w+')
try:
    writer = csv.writer(csvFile)
    #3개의 열을 추가함
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        #그 열에 i를 넣음
        writer.writerow((i, i+2, i*2))
#try에서 예외 발생 관계 없이 무조건 실행됨
finally:
    csvFile.close()
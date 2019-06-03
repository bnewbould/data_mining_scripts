import csv

class BreakoutException(Exception):
    pass

def main():
    with open('testSet.txt', errors="replace") as file:
        lines = file.readlines()
        separator = "-"
        file_out = open('clean_set.txt', 'w', newline='')
        for att in csv.reader(lines, quotechar='\'', delimiter=','):
            text = att[8]
            try:
                for char in text:
                    if 65 <= ord(char) <= 120:
                       raise BreakoutException
                continue
            except BreakoutException:
                pass
            csvwriter = csv.writer(file_out,quotechar='\'', delimiter=',')
            try:
                csvwriter.writerow(att)
            except:
                print("reeeeee")
                continue
        file.close()
    
if __name__ == "__main__":
    main()

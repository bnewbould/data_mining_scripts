import csv

class BreakoutException(Exception):
    pass

def main():
    with open('files/clean_fixed_set.txt', errors="replace") as file:
        lines = file.readlines()
        file_out = open('files/even_clean_set.txt', 'w', newline='')
        pos = 0
        neg = 0
        output = []
        csvwriter = csv.writer(file_out,quotechar='\'', delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for att in csv.reader(lines, quotechar='\'', delimiter=','):
            try:
                if att[6] == '0':
                    if neg < 5000:
                        neg+=1
                        raise BreakoutException
                else:
                    if pos < 5000:
                        pos+=1
                        raise BreakoutException
            except BreakoutException:
                try:
                    csvwriter.writerow(att)
                except:
                    print("reeeeee")
                    continue
            if pos >= 5000 and neg >= 5000:
                print('it\'s all ogre')
                break
        file_out.close()
        file.close()
        
if __name__ == "__main__":
    main()

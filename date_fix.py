import csv

def main():
    with open('testSet.txt', errors="replace") as file:
        lines = file.readlines()
        separator = "-"
        file_out = open('fixed_set.txt', 'w', newline='')
        for att in csv.reader(lines, quotechar='\'', delimiter=','):
            date_split = att[7].split()
            day = date_split[0].zfill(2)
            month = month_to_number(date_split[1])
            year = date_split[2]
            date = day + separator + month + separator + year
            output = []
            for i in range(10):
                if i != 7:
                    output.append(att[i])
                else:
                    output.append(date)
            csvwriter = csv.writer(file_out,quotechar='\'', delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
            try:
                csvwriter.writerow(output)
            except:
                print("reeeeee")
                continue
        file.close()
        

def month_to_number(month_name):
    month_dictionary = {'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06',
                        'jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12'}
    abbr = month_name.strip()[:3].lower()
    return month_dictionary[abbr]
    
if __name__ == "__main__":
    main()

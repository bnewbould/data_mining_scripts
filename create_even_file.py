def main():
    f = open('testSet.txt', errors="replace")
    lines = f.readlines()
    fout = open('even_set.txt', 'w')
    pos = 0
    neg = 0
    for line in lines:
        if line[-2] == '0':
            if neg < 5000:
                neg+=1
                fout.write(line)
        else:
            if pos < 5000:
                pos+=1
                fout.write(line)
        if pos >= 5000 and neg >= 5000:
            print('it\'s all ogre')
            break
        

if __name__ == "__main__":
    main()

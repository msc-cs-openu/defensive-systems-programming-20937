def main():
    line = 'This line contains words and some have the letter o'
    o_list = [w.upper() for w in line.split() if 'o' in w]

    print(*o_list, sep=', ')


if __name__ == '__main__':
    main()

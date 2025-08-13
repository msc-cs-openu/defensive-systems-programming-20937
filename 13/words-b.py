def main():
    a_list = ["apple", "banana", "carrot", "black", "box"]
    b_list = [w.capitalize() for w in a_list if w.startswith('b')]

    print(f"a_list: {a_list}, b_list: {b_list}")


if __name__ == '__main__':
    main()

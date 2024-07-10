from executor import execute_query


def main():
    query = input("what would you like to know? ")
    result = execute_query(query)
    print("Result: ")


if __name__ == "__main__":
    main()

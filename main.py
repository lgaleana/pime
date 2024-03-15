import api


def main():
    params = {}
    response = api.search_flights(params)
    print(response)


if __name__ == '__main__':
    main()

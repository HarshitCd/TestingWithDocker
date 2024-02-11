def test_func(data: list[str]) -> str:
    return " - ".join(data)


def main():
    print(test_func(["Hello", "world"]))


if __name__ == "__main__":
    main()

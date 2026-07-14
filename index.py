from utils import calculate

def main():
    keep_calculating_count = 3
    while keep_calculating_count >= 1:
        calculate()
        keep_calculating_count = keep_calculating_count - 1
        print(f"remain calculation: {keep_calculating_count}")

if __name__ == "__main__":
    main()        



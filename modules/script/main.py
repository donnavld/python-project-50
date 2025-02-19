import argparse

def main():
    print("Hello from python-project-50!")
    parser = argparse.ArgumentParser(
                    prog='hexlet-code',
                    description='Compares two configuration files and shows a difference.',
                    epilog='Enter 2 foles')
    parser.add_argument("first_file", help="Path to the first configuration file")
    parser.add_argument("second_file", help="Path to the second configuration file")
    args = parser.parse_args()
    
    # Здесь будет логика вычисления отличий между файлами
    print("Difference Calculator is not implemented yet.")


if __name__ == "__main__":
    main()



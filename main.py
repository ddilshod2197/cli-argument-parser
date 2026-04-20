import argparse

def main():
    parser = argparse.ArgumentParser(description='CLI argument parser')
    parser.add_argument('-n', '--name', help='Ismni kiriting')
    parser.add_argument('-a', '--age', type=int, help='Yoshni kiriting')
    parser.add_argument('-c', '--city', help='Shaharni kiriting')
    args = parser.parse_args()

    if args.name:
        print(f"Ism: {args.name}")
    if args.age:
        print(f"Yosh: {args.age}")
    if args.city:
        print(f"Shahar: {args.city}")

if __name__ == "__main__":
    main()
```

```bash
python script.py -n Ali -a 25 -c Toshkent
```

Kodni ishga tushirish uchun quyidagilarni amalga oshiring:

1. Kodni yozuvchi faylga saqlang (masalan, `script.py`).
2. Kompyuterda terminalga kirib, quyidagi buyruqlarni bosing:
   - `python script.py -h` - CLI argument parser haqida ma'lumot olish.
   - `python script.py -n Ali -a 25 -c Toshkent` - CLI argument parserni ishga tushirish.

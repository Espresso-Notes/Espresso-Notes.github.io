from pathlib import Path


def main():
    base_path = Path('.')
    with open(base_path / 'manifest.csv', 'w') as manifest:
        for dir in base_path.iterdir():
            if dir.is_dir():
                write_files(dir, manifest)


def write_files(path: Path, manifest):
    for file in path.iterdir():
        if file.is_dir():
            write_files(file, manifest)
        elif file.is_file() and '.py' not in str(file):
            manifest.write(f'{str(file)}\n')


if __name__ == '__main__':
    main()

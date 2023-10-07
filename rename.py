import os


def rename_files(path_to_files, new_name, digit_count_suffix=0, target_file_ext='', new_ext='', range_name=None):
    assert digit_count_suffix >= 0, 'digit_count_suffix должен быть >= 0'
    files = os.listdir(path_to_files)
    if digit_count_suffix == 0:
        file_count = len(files)
        digit_count_suffix = 1
        while file_count // 10 != 0:
            digit_count_suffix += 1
            file_count //= 10

    counter = 1
    for filename in files:
        if filename.endswith(target_file_ext):
            old_name_prefix = ''
            if range_name is not None:
                old_name_prefix = filename[range_name[0]:range_name[1]]
            new_filename = f"{old_name_prefix}{new_name}{str(counter).zfill(digit_count_suffix)}{new_ext}"
            os.rename(os.path.join(path_to_files, filename), os.path.join(path_to_files, new_filename))
            counter += 1


def generate_file(path, name, count, ext = ''):
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(1, count + 1):
        with open(f'{path}/{name}{str(i)}{ext}', 'w'):
            pass


generate_file(path='tests', name='test', count=10)
generate_file(path='tests', name='test', count=10, ext='.txt')
rename_files(path_to_files='tests', new_name='new_file', target_file_ext='.txt', range_name=[0, 3], new_ext='.tst')
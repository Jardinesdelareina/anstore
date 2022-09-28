from django.core.exceptions import ValidationError

def get_path_upload_avatar(instance, file):
    # Построение пути к файлу аватара
    return f'avatar/user_{instance.id}/{file}'

def validate_size_avatar(file_obj):
    # Валидация размера загружаемого аватара
    size_limit = 3
    if file_obj > size_limit * 1024 * 1024:
        return ValidationError(f'Максимальный размер загружаемого файла {size_limit}Mb')

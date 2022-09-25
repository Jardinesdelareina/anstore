from django.core.exceptions import ValidationError

def validate_size_image(file_obj):
    # Валидация размера загружаемого аватара
    size_limit = 1
    if file_obj > size_limit * 1024 * 1024:
        return ValidationError(f'Максимальный размер загружаемого файла {size_limit}Mb')

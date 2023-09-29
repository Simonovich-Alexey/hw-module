from datetime import datetime
from rembg import remove
from PIL import Image
from application.salary import calculate_salary
from application.db.people import get_employees


def dell_bg(input_path, output_path):
    """
    Функция удаляет фон у изображения
    :param input_path: Путь до изображения у которого надо удалить фон
    :param output_path: Название изображения в который сохраняем результат
    """
    open_file = Image.open(input_path)
    output = remove(open_file)
    output.save(output_path)
    print(f'Фон изображения удален!: {datetime.today().date()}')


if __name__ == "__main__":
    calculate_salary()
    get_employees()

    dell_bg('duck.jpg', 'output_duck.png')

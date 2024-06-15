import os
import pandas as pd
from django.core.management.base import BaseCommand
from django.conf import settings
from support.models import QuestionAnswer

class Command(BaseCommand):
    help = 'Импорт данных из файла Excel в модель QuestionAnswer'

    def add_arguments(self, parser):
        parser.add_argument('relative_path', type=str, help='Относительный путь к файлу Excel от базового каталога')

    def handle(self, *args, **kwargs):
        relative_path = kwargs['relative_path']
        file_path = os.path.join(settings.BASE_DIR, relative_path)
        
        self.stdout.write(self.style.SUCCESS(f'Импорт данных из {file_path}'))
        
        df = pd.read_excel(file_path, header=None)

        # # Получаем первую строку (заголовки) и присваиваем её столбцам
        # headers = df.iloc[0]
        # df = df[1:]  # Пропускаем первую строку
        # df.columns = headers

        # # Теперь df содержит данные с корректными заголовками столбцов
        # print(df.head())  # Печатаем первые несколько строк для проверки
        
        try:
            df = pd.read_excel(file_path, header=1)
            # print(list(df.iterrows())[1])
            for index, row in df.iterrows():
                # print(row['Описание'])
                QuestionAnswer.objects.create(
                    question=row['Описание'],
                    answer=row['Решение']
                )

            self.stdout.write(self.style.SUCCESS('Данные успешно импортированы'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при импорте данных: {e}'))

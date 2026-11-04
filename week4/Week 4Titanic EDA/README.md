# Titanic: очистка данных и анализ

Учебный проект на данных Kaggle «Titanic: Machine Learning from Disaster».

## Файлы

- `01_cleaning.ipynb` — очистка данных: закрытие пропусков, новые признаки (`HasCabin`, `FamilySize`, `IsAlone`), сохранение `train_clean.csv`.
- `02_questions.ipynb` — ответы на вопросы по очищенным данным.

## Данные

Файл с данными **в репозиторий не включён**. Перед запуском скачайте `train.csv` со страницы соревнования:
https://www.kaggle.com/c/titanic/data

Положите его в папку с ноутбуками и **назовите `train-2.csv`** — именно под этим именем его читает `01_cleaning.ipynb`. Без этого файла первая ячейка упадёт с `FileNotFoundError`.

## Запуск

```bash
pip install pandas matplotlib jupyter
jupyter notebook
```

1. Откройте и выполните `01_cleaning.ipynb` (Restart → Run All). Он создаст `train_clean.csv`.
2. Затем выполните `02_questions.ipynb`.

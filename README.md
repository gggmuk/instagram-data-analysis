# 📊 Instagram Data Analysis

Аналитика данных Instagram с использованием Python, pandas и визуализацией.

## 📈 О проекте

Скрипты для анализа метрик Instagram: подписчики, лайки, посты и engagement rate.

## 🔧 Технологии

- **Python 3.10+**
- **pandas** — обработка данных
- **numpy** — численные вычисления
- **matplotlib** — визуализация
- **seaborn** — статистические графики

## 📦 Структура

```
asel/
├── 3lab.py                    # Описательная статистика и визуализация
├── 4lab.py                    # Корреляционный анализ
├── .venv/                     # Виртуальное окружение
└── README.md
```

## 🚀 Запуск

### Установка зависимостей
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
pip install pandas numpy matplotlib seaborn
```

### Запуск скриптов
```bash
python 3lab.py    # Описательная статистика
python 4lab.py    # Корреляционный анализ
```

## 📊 Результаты

Скрипты создают:
- `descriptive_stats_visual.png` — гистограммы с KDE
- `outliers_analysis.png` — диаграммы "ящик с усами"
- `correlation_heatmap.png` — тепловая карта корреляций

## 📄 Лицензия

MIT

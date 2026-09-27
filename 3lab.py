import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Установка эстетичного стиля
sns.set_theme(style="white")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 120

# Генерируем данные, максимально близкие к метрикам из Задания III
np.random.seed(42)
n = 50

# Функция для подбора логнормального распределения по среднему и медиане
# median = exp(mu), mean = exp(mu + sigma^2/2)
def gen_skewed(target_mean, target_median, n_samples):
    mu = np.log(target_median)
    sigma = np.sqrt(2 * (np.log(target_mean) - mu))
    res = np.random.lognormal(mu, sigma, n_samples)
    return res

# 1. posts_count (mean=185.5, median=170) -> Почти симметрично
posts_count = np.random.normal(185, 60, n)
posts_count = np.clip(posts_count, 40, 350)

# 2. followers (mean=11200, median=9500) -> Положительная асимметрия
followers = gen_skewed(11200, 9500, n)
followers = np.clip(followers, 500, 40000)

# 3. likes_total (mean=31500, median=25000) -> Выраженная асимметрия
likes_total = gen_skewed(31500, 25000, n)
likes_total = np.clip(likes_total, 3000, 95000)

# 4. engagement_rate (mean=2.85, median=2.5)
engagement_rate = gen_skewed(2.85, 2.5, n)
engagement_rate = np.clip(engagement_rate, 0.8, 7.5)

df = pd.DataFrame({
    'posts_count': posts_count,
    'likes_total': likes_total,
    'followers': followers,
    'engagement_rate': engagement_rate
})

# Названия на русском для графиков
titles = {
    'posts_count': 'Количество постов',
    'likes_total': 'Суммарные лайки',
    'followers': 'Количество подписчиков',
    'engagement_rate': 'Engagement Rate (%)'
}

# Визуализация комплексная
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
colors = sns.color_palette("viridis", 4)

for i, col in enumerate(df.columns):
    ax = axes[i // 2, i % 2]
    
    # Гистограмма с KDE
    sns.histplot(df[col], kde=True, ax=ax, color=colors[i], alpha=0.6)
    
    # Добавляем линии среднего и медианы
    mean_val = df[col].mean()
    median_val = df[col].median()
    ax.axvline(mean_val, color='red', linestyle='--', label=f'Среднее: {mean_val:.1f}')
    ax.axvline(median_val, color='blue', linestyle='-', label=f'Медиана: {median_val:.1f}')
    
    ax.set_title(f'Распределение: {titles[col]}', fontsize=14, fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylabel('Частота')
    ax.legend()

plt.tight_layout(pad=3.0)
plt.savefig('descriptive_stats_visual.png')

# Визуализация Boxplots отдельно для сравнения масштабов (без вовлеченности, так как единицы разные)
plt.figure(figsize=(12, 6))
cols_to_plot = ['posts_count', 'followers'] # Разные масштабы, но для примера
# Лучше сделать нормализованный или просто отдельные боксплоты
fig, axes = plt.subplots(1, 4, figsize=(20, 6))
for i, col in enumerate(df.columns):
    sns.boxplot(y=df[col], ax=axes[i], color=colors[i], width=0.5)
    axes[i].set_title(titles[col], fontsize=12)
    axes[i].set_ylabel('')

plt.suptitle('Диаграммы "ящик с усами" (Boxplots) для выявления выбросов', fontsize=16)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('outliers_analysis.png')

print("Описательная статистика сгенерированных данных:")
stats = df.describe().T[['mean', '50%', 'std', 'min', 'max']]
stats.columns = ['Среднее', 'Медиана', 'Ст. откл.', 'Мин', 'Макс']
print(stats)
print("\nВизуализации сохранены в 'descriptive_stats_visual.png' и 'outliers_analysis.png'")

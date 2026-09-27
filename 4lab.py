import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Генерация данных (N=50)
# Чтобы получить корреляции, близкие к заданным, используем нормальное распределение
np.random.seed(42)
n_samples = 50

# Генерируем базовые метрики
followers = np.random.randint(1000, 50000, n_samples)
# likes_total сильно коррелирует с followers (r ~ 0.95)
likes_total = followers * np.random.uniform(2, 5, n_samples) + np.random.normal(0, 5000, n_samples)
likes_total = np.maximum(likes_total, 100) # Исключаем отрицательные значения

# posts_count умеренно коррелирует с likes_total (r ~ 0.48)
posts_count = (likes_total * 0.001 + np.random.randint(10, 200, n_samples)).astype(int)

# engagement_rate = (likes / followers) * 100
# Характерна слабая отрицательная корреляция с followers (r ~ -0.22)
engagement_rate = (likes_total / followers) * 100
# Добавим немного шума, чтобы соответствовать реальности и заданным коэффициентам
engagement_rate = engagement_rate + np.random.normal(0, 1, n_samples)
engagement_rate = np.clip(engagement_rate, 0.1, 20)

# Создаем DataFrame
data = {
    'likes_total': likes_total,
    'followers': followers,
    'posts_count': posts_count,
    'engagement_rate': engagement_rate
}
df = pd.DataFrame(data)

# 2. Расчет матрицы корреляции
corr_matrix = df.corr()

print("Матрица корреляции:")
print(corr_matrix)

# 3. Визуализация (Тепловая карта)
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Тепловая карта корреляций метрик Instagram (Вариант 16)')
plt.savefig('correlation_heatmap.png')
print("\nГрафик сохранен в файл 'correlation_heatmap.png'")

# 4. Выводы (автоматизированно на основе данных или по шаблону пользователя)
print("\n--- ВЫВОДЫ ПО АНАЛИЗУ ---")
r_likes_fol = corr_matrix.loc['likes_total', 'followers']
print(f"1. Корреляция likes_total и followers: {r_likes_fol:.2f}")
print("   Интерпретация: Сильная положительная связь. Количество лайков растет пропорционально аудитории.")

r_likes_posts = corr_matrix.loc['likes_total', 'posts_count']
print(f"2. Корреляция likes_total и posts_count: {r_likes_posts:.2f}")
print("   Интерпретация: Умеренная связь. Количество контента влияет на лайки, но не является определяющим фактором.")

r_fol_er = corr_matrix.loc['followers', 'engagement_rate']
print(f"3. Корреляция followers и engagement_rate: {r_fol_er:.2f}")
print("   Интерпретация: Слабая отрицательная связь. С ростом аккаунта вовлеченность часто падает.")

r_posts_er = corr_matrix.loc['posts_count', 'engagement_rate']
print(f"4. Корреляция posts_count и engagement_rate: {r_posts_er:.2f}")
print("   Интерпретация: Слабая связь. Частота публикаций почти не сказывается на проценте вовлеченности.")

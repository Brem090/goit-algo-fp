import random
import matplotlib.pyplot as plt

throws = 1000000
sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(throws)]

frequency = {}
for sum_val in sums:
    if sum_val in frequency:
        frequency[sum_val] += 1
    else:
        frequency[sum_val] = 1

probabilities = {sum_val: (count / throws) * 100 for sum_val, count in frequency.items()}
sorted_probabilities = dict(sorted(probabilities.items()))

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

plt.figure(figsize=(10, 6))
plt.bar(sorted_probabilities.keys(), sorted_probabilities.values(), color='blue', label='Метод Монте-Карло')
plt.plot(list(analytical_probabilities.keys()), list(analytical_probabilities.values()), 
         color='red', marker='o', linestyle='dashed', linewidth=2, markersize=8, label='Аналітичний розрахунок')
plt.title('Розподіл ймовірностей суми двох кидків кубиків')
plt.xlabel('Сума двох кубиків')
plt.ylabel('Ймовірність (%)')
plt.xticks(range(2, 13))
plt.yticks(range(0, 18, 2))
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print(sorted_probabilities)

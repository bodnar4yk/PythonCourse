# one_point=['a','b','c','o']
# two_point=['d','f']
# ten_point=['z']

# def calculate_score(word):
#     score=dict.fromkeys(one_point,1)|dict.fromkeys(two_point,2)|dict.fromkeys(ten_point,10)
#     result = {n: count for n in score.keys() if (count := word.count(n)) > 0}
#     total_result={key: score[key]*result[key] for key in result.keys()&score.keys()}
#     sum_score=sum(total_result.values())
#     print(sum_score)
#     #return total_score

# calculate_score('bookzz')

from collections import Counter

one_point = ['a', 'b', 'c', 'o']
two_point = ['d', 'f']
ten_point = ['z']

# Створюємо словник вартості один раз поза функцією
score_map = {**dict.fromkeys(one_point, 1), 
             **dict.fromkeys(two_point, 2), 
             **dict.fromkeys(ten_point, 10)}

def calculate_score(word):
    # Counter рахує всі літери за один прохід: {'b': 1, 'o': 2, 'k': 1, 'z': 2}
    counts = Counter(word)
    
    # Рахуємо суму: беремо кількість літери та множимо на її ціну зі словника
    # .get(char, 0) поверне 0, якщо літери немає в списку балів
    total_sum = sum(counts[char] * score_map.get(char, 0) for char in counts)
    
    print(total_sum)

calculate_score('bookzz') # b(1) + o(1)*2 + z(10)*2 = 23
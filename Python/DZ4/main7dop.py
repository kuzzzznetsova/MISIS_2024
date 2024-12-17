def word_count(phrase):
    # Токенизация строки на отдельные слова
    words = phrase.split()

    # Подсчет количества слов
    number_of_words = len(words)

    # Печать каждого слова
    for word in words:
        print(word)

    # Печать общего количества слов
    print(f"Number of Words: {number_of_words}")

    # Подсчет и вывод процента для каждого слова
    print("\nПроцентное соотношение каждого слова:")
    for word in words:
        word_weight = (phrase.count(word) / number_of_words) * 100
        print(f"{word}: {word_weight:.2f}%")

word_count("Тут фраза с пробелами и я хочу их распечатать по одному на строку и ещё посчитать слова")

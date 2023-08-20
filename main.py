"""
The first test version of the chatbot
Course project after completing the Python Started course

"""
import pyjokes
import game_guess_the_number
import game_stone_scissors_paper
import interested_history
# import logo


def main():
    """
    The main function that handles user interactions with the chatbot.

    This function displays the bot's capabilities and instructions to the user.
    It repeatedly takes user input and provides responses from the chat_bot function.

    Returns: None
    """
    # print(logo.logo())
    print("Відповідати на деякі питання\n"
          "Допомогаю з вибором цікавих фільмів\n"
          "Допомогаю з вибором музики популярних виконавців\n"
          "Маю декілька ігр, шоб не сумувати\n"
          "Маю декілька цікавих історій\n"
          "Для виходу введіть 'вийти'")
    print()
    print("Привіт! Я чат-бот 'Інтерактивний Компаньйон'. Задавайте свої"
          "запитання або напишіть 'вийти', щоб завершити.")

    while True:
        user_input = input("Ви: ")
        if user_input.lower() == "вийти":
            print("До побачення!")
            break
        response = chat_bot(user_input)
        print("Бот:", response)


def chat_bot(question):
    """
    Generates appropriate responses based on user input keywords.

    Args:
    question (str): User input text.

    Returns:
    str: Response to the user's input.
    """
    responses = {
        "привіт": "Привіт! Я тут, щоб допомогти.",
        "як справи": "Все гаразд, дякую! Як я можу вам допомогти?",
        "погода": "Зараз на вулиці гарна погода.",
        "фільми": films,
        "музика": musics,
        "анекдот": jokes,
        "ігри": games,
        "історії": display_story
    }

    question_lower = question.lower()

    for keyword, response in responses.items():
        if keyword in question_lower:
            if callable(response):
                return response()
            return response
    print("Вибачте, я не розумію це питання.")


def films():
    """
    Provides information about movies based on user input.

    Returns:
    None
    """
    films_by_genre = {
        "комедія": ["Форрест Гамп", "1+1", "Інтерв'ю з вампіром"],
        "драма": ["Шоу Трумана", "Зелена миля", "Побутовий роман"],
        "фантастика": ["Матриця", "Інтерстеллар", "Вовк з Уолл-стріт"],
        "екшн": ["Термінатор 2: Судний день", "Месники", "Джон Вік"],
    }

    search_genre = input("Введіть жанр фільмів: ").lower()

    if search_genre in films_by_genre:
        print(f"Фільми у жанрі '{search_genre}': {', '.join(films_by_genre[search_genre])}")
    else:
        print(f"Фільми у жанрі '{search_genre}' не знайдено.")


def musics():
    """
    Provides information about music based on user input.

    Returns:
    None
    """
    music_by_genre = {
        "класична музика": ["Вагнер", "Бах", "Моцарт", "Бетховен"],
        "рок-н-рол": ["Адріано Челентано", "Оззі Осборн", "Пол Маккартні"],
        "рок": ["The Beatles", "Rammstein", "Linkin park", "System of a Down"],
        "поп": ["Майкл Джексон", "Мадонна", "Ріанна", "Елвіс Преслі"],
    }

    search_genre = input("Введіть жанр музики: ").lower()

    if search_genre in music_by_genre:
        print(f"Музика у жанрі '{search_genre}': {', '.join(music_by_genre[search_genre])}")
    else:
        print(f"Музика у жанрі '{search_genre}' не знайдена.")


def jokes():
    """
    Generates and displays a random joke.

    Returns:
    str: A random joke.
    """
    joke = pyjokes.get_joke()
    return joke


def games():
    """
    Offers various games for the user to play.

    Returns:
    None
    """
    print("Давайте зіграємо в гру! Оберіть гру, введіть номер:")
    print("1. Вгадай число")
    print("2. Камень ножиці та папір")

    choice = input("Ваш вибір: ")

    if choice == "1":
        game_guess_the_number.game_guess_the_number()
    elif choice == "2":
        game_stone_scissors_paper.game_stone_scissors_paper()
    else:
        print("Некоректний вибір. Спробуйте ще раз.")


def display_story():
    """
    Displays an interesting history story based on user input.

    Returns:
    None
    """
    print("1. Звуковий бар’єр\n"
          "2. Таблиця множення\n"
          "3. Куди плавали вікінги?\n"
          "4. Хто придумав алфавіт\n"
          "5. Теорема Байєса\n"
          "6. Що таке нескінченність?")

    stories_dict = interested_history.interested_history()
    user_choice = input("Виберіть число від 1 до 6: ")

    if user_choice.isdigit() and 1 <= int(user_choice) <= 6:
        story_number = int(user_choice)
        story = stories_dict[story_number]
        print(story)
    else:
        print("Некоректний вибір. Спробуйте ввести число від 1 до 6.")


if __name__ == "__main__":
    main()

"""
A function with a dictionary is created, where the key is an arbitrary number, the value is a story.
"""
def interested_history():
    """
    Provides a dictionary containing interesting historical stories.

    Returns:
    dict: A dictionary where keys are story numbers and values are corresponding stories.
   """
    stories_dict = {
        1: "Звуковий бар’єр — це просто набір складнощів з якими стикається літак, коли його\n"
           "швидкість наближається до швидкості звукуНемає жодного значення швидкості,\n"
           "яка характеризує звуковий бар’єр. Для кожного літака (і не тільки літака) буде\n"
           "своє значення швидкості, коли виявляються пов’язані із надзвуком проблеми Проблеми\n"
           "літального апарату можуть виникнути ще до того, як він досягне швидкості звуку\n "
           "Завдання подолання звукового бар’єру вирішується по-різному. Суть цього завдання —\n"
           "знизити негативні наслідки від надзвукової швидкості та не надто погіршити\n"
           "характеристики дозвукового польоту. Так що насправді заважає літаку подолати звуковий\n"
           "бар’єр? Справа в тому, що при досягненні швидкості звуку характер обтікання\n"
           "повітрям літака різко змінюється. Літак ніби потрапляє в інше середовище,\n"
           "де діють інші закони.Тут важливо ще раз обмовитися, саме ніби. Насправді середовище\n"
           "те саме, це навколишнє повітря, тільки поведінка його вже змінилася.",
        2: "Прийнято вважати, що це був Піфагор. І той самий давньогрецький математик, який довів\n"
           "теорему про прямокутний трикутник. Ось тільки археологи знайшли таблиці множення,\n"
           "які були створені до Піфагора і не в Греції. Перша така знахідка старша за Піфагор\n"
           "приблизно на п’ятсот років і знайдена була у Вавилоні.Цікаво, що виглядала ця таблиця\n"
           "множення зовсім незвично, тому що вавилонянка математика була заснована на\n"
           "шестидесятиричній системі числення, а не на десятковій. Десятичну таблицю множення\n"
           "виявили в Китаї, але дуже малоймовірно, що Стародавній Китай мав стійкі зв’язки\n"
           "з Стародавньою Грецією.Чи правда, що саме Піфагор винайшов таблицю множення\n"
           "не відомо. Адже ніяких документів, що доводять це не збереглося, та й не\n "
           "використовували греки в ті часи цифри, які ми зараз називаємо арабськими.",
        3: "Почнемо з недалеких походів до Європи. Вікінги починаючи з 8-го століття\n"
           "нашої ери Вікінги відвідували Англію з метою пограбування. Це називалося “вікінг”,\n"
           "тобто — “похід”. Самих прибульців англійці називали данами (хоча припливали\n"
           "вікінги як з Данії так і з Норвегії).У дев’ятому столітті вікінги захопили\n"
           "навіть Лондон.Аж до в 1066 року королями Англії були то норвежці, то датчани,\n"
           "поки Вільгельм Завойовник не прибув із Франції. Вільгельм був герцогом Нормандії,\n"
           "тобто також скандинавом за походженням.",
        4: "Першим у світі алфавітом вважається — фінікійський. Звичайно, є безліч теорій,\n"
           "його походження, але жодна серйозна теорія не заперечує першості.\n"
           "Саме фінікійці створили перший алфавіт.Можливо, фінікійці вигадали літери\n"
           "не на порожньому місці, можливо і у них були попередники. Але цілком очевидно,\n"
           "що практично всі літери сучасних азбук — фінікійські нащадки.Це були перші літери\n"
           "в історії. На відміну від ієрогліфів, якими користувалися єгиптяни, літера\n"
           "означала один звук, а не об’єкт чи поняття. Таким чином, для запису слова,\n"
           "хоч і потрібно більше дій (кілька букв замість однієї картинки), але самих букв\n"
           "потрібно знати набагато менше.",
        5: "Оцінювати ймовірності складно, нам простіше думати про події з точки зору “точно”\n"
           "(ймовірність = 1) і “неможливо” (ймовірність = 0). Але світ не такий простий, часто\n"
           "потрібно враховувати не лише ймовірність однієї події, а одразу кількох. Для цього існує\n"
           "теорема Байєса. Теорема Байєса простими словамиНайкращий спосіб зрозуміти\n"
           "теорему Байєса — на прикладі, де головний герой… це ви. Уявимо, що ви захворіли.\n"
           "Лікар призначив аналіз, точність якого 97%. Цей тест показав, що ви заражені\n"
           "вірусом Х, який і викликав недугу.При цьому відомо, що ймовірність заразиться\n"
           "вірусом Х у вашій країні лише 1%. Він дуже рідкісний, а ви нікуди не виїжджали\n"
           "останнім часом. Головне питання: лікуватися чи ні? Є ймовірність захворіти 1%\n"
           "і ймовірність того, що тест правильно визначив вірус у 97% (3% залишається на помилку)\n"
           "Перш ніж читати далі відповідайте на запитання в коментарі, з якою ймовірністю ви\n"
           "дійсно хворі? Потім поверніться до тексту і порахуйтецю можливість за допомогою\n"
           "формули Байєса Отже, більшість людей будуть схильні вважати, що вони дійсно\n"
           "заразилися вірусом Х, адже тест точний на 97%, а це “майже 100”. Але давайте порахуємо.",
        6: "Нескінченність — складна для розуміння штука. У звичайному житті ми не зустрічаємося з чимось,\n"
           "у чого немає початку і кінця. Тим більш дивно, що така абстракція зустрічається так часто:\n"
           "і у фізиці, і в математиці і, звичайно, в релігії з філософією, де, це якраз дуже виправдано.\n"
           "Адже лише політ фантазії і може бути по-справжньому безкінечним.",
    }
    return stories_dict

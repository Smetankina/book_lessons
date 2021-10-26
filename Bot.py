import random

BOT_CONFIG = {
    'intents':{
        "hello":{
            'examples': ['Привет', 'Добрый день', 'Шалом', 'здравствуйте'],
            'responses': ['Привет, человек', 'Доброго времени суток']
        },
    'bye':{
        'examples': ['Пока', 'Досвидания', 'Прощайте', 'До свидания'],
        'responses': ['Счастиливо', 'Если что я тут', 'Еще увидимся']
    }
    },
    'failure_phrases': [
        'Попробуйте написать по-другому'
        'Что-то непонятно'
        'Я же всего лишь бот'
    ]}

intent = input()

def get_intent(intent):
    for intent in BOT_CONFIG['intents']:
        print[intent]


def get_answer_by_intent(intent):
    if intent in BOT_CONFIG['intents']:
        phrases = BOT_CONFIG['intents'][intent]['responses']
        return random.choice(phrases)

def generate_answer_by_text(question):
    return #TODO 3th day


def get_failure_phrase():
    phrases = BOT_CONFIG['failure_phrases']
    return random.choice(phrases)


def bot(question):

    #NLU
    intent = get_intent(question)
    #Получение ответа
    if intent:
        answer = get_answer_by_intent(intent)
        if answer:
            return answer

    #Генерируем  ответ
    answer = generate_answer_by_text(question)
    if answer:
        return answer
    #Заглушка
    answer = get_failure_phrase()
    return answer




"""
question = None
     while question != 'exit':
        question = input()   
    answer = question
    print(answer)"""

bot(question='hello')
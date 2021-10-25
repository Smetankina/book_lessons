def get_intent(question):
    return 'hello'


def get_answer_by_intent(intent):
    if answer == 'hello':
        return "Привет"

def generate_answer_by_text(question):
    return #TODO 3th day


def get_failure_phrase():
    return 'Я не поняла'

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


question = None

#while question in ['exit', 'выход']:
while question != 'exit':
    question = input()
    answer = question
    print(answer)

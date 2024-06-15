from gradio_client import Client


# GPT_URL = "https://qwen-qwen1-5-72b-chat.hf.space/--replicas/061qr/"
GPT_URL = "https://qwen-qwen1-5-110b-chat-demo.hf.space/"

def query_predict_nlp(input_message, promt):
    client = Client(GPT_URL)
    result = client.predict(
        input_message,
        # context,
        [["None", "None"]],
        promt,
        api_name="/model_chat"
        )
    return result[1][1][1]

# promt = """Участники должны предложить решение, которое приведет к уменьшению количества обращений,
#  основанное на использовании технологий искусственного интеллекта.
#  Решение должно иметь возможность отвечать на вопросы пользователей,
#  сохранять контекст обращения и вести статистику запросов пользователей.
#  Обращаем ваше внимание, что используемые технологии должны быть доступны для коммерческого использования на территории РФ.
#  Решение не должно иметь компонентов от вендоров, покинувших территорию России."""
 
# question = "Выдели из текста, что должен сделать участник? :"
# answer = query_predict_nlp(question, promt)
# print(answer)

# context = "Твои прошлые ответы: " + promt + question + answer
# question_2 = "Дай короткий ответ!"
# answer_2 = query_predict_nlp(question_2, context)
# print(answer_2)

# context = "Твои прошлые ответы: " + context + question_2 + answer_2
# question_3 = "Что ещё можешь добавить?"
# answer_3 = query_predict_nlp(question_3, context)
# print(answer_3)
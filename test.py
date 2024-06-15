# from gradio_client import Client


# GPT_URL = "https://qwen-qwen1-5-72b-chat.hf.space/--replicas/061qr/"

# def query_predict_nlp(input_message, promt):
#     client = Client(GPT_URL)
#     result = client.predict(
#         input_message,
#         # context,
#         [["None", "None"]],
#         promt,
#         api_name="/model_chat"
#         )
#     return result[1][1][1]

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

# import re

# def remove_chinese_chars(text):
#     cleaned_text = re.sub(r'[\u4e00-\u9fff]', '', text)
#     return cleaned_text

# # Пример использования
# text = "Привет, 你好! Как дела?"
# cleaned_text = remove_chinese_chars(text)
# print(cleaned_text)
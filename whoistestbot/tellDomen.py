import whois
import json

def domenTell(message):
    w = whois.whois(message)
    j = json.loads(str(w))
    return "Имя домена: " + str(j['domain_name']) + "\n\n" + "Ваш регистратор: " + str(j['registrar']) + "\n\n" + \
           "Дата создания домена: " + str(j['creation_date']) + "\n\n" + "Домен продлен до: " + str(j['expiration_date']) + \
           "\n\n" + "Длегирован на серверах: " + "\n" + str(j['name_servers'])



# try:
#     def domenTell(message):
#         w = whois.whois(message)
#         j = json.loads(str(w))
#         return "Имя домена: " + str(j['domain_name']) + "\n\n" + "Ваш регистратор: " + str(j['registrar']) + "\n\n" + \
#                "Дата создания домена: " + str(j['creation_date']) + "\n\n" + "Домен продлен до: " + str(j['expiration_date']) + \
#                "\n\n" + "Длегирован на серверах: " + "\n" + str(j['name_servers'])
# except Exception:
#     print('Ну зачем вы сделали мне EOF?')
# # except KeyboardInterrupt:
# #     print('Вы отменили операцию.')
# else:
#     print('Хм')


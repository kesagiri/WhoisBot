import whois
import json

try:
    def domenTell(message):
        w = whois.whois(message)
        j = json.loads(str(w))
        return "Имя домена: " + str(j['domain_name']) + "\n\n" + "Ваш регистратор: " + str(j['registrar']) + "\n\n" + \
               "Дата создания домена: " + str(j['creation_date']) + "\n\n" + "Домен продлен до: " + str(
            j['expiration_date']) + \
               "\n\n" + "Делегирован на серверах: " + "\n" + str(j['name_servers'])
except ValueError:
    print("Ничего нет")


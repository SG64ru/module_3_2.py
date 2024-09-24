

def send_emal(message, recipient, sender = "university.help@gmail.com"):

    if "@" not in recipient and ".com" not in recipient and ".ru" in recipient and ".net" in recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        if sender == recipient:
            print("Нельзя отправлять письмо самому себе!")
        else:
            if sender == "university.help@gmail.com":
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")

            else:
                print("Нестандартный отправитель")

send_emal("Это сообщение для проверки связи", "vasyok1337@gmail.com", sender = "university.help@gmail.com")

start = "Добро пожаловать, я робот компании Timeweb! Я могу помочь Вам решить некоторые вопросы." \
       + "\n\n" + \
       "Управлять мной Вы можете через следующие команды:" \
       + "\n\n" + \
       "<b>Оплата</b>" + "\n" \
       + '/pay' + " - скажу как оплатить" \
       + "\n\n" + \
       "<b>Домены</b>" + "\n" \
       '/change_admin' + " - скажу, как сменить администратора домена" \
       + "\n" + \
       '/domain_transfer' + " - скажу, как сделать технический или административный перенос домена" \
       + "\n" + \
       '/difference' + " - скажу, чем отличается технический перенос от административного" \
       + "\n" + \
       '/whois' + " - покажу информацию по домену" \
       + "\n\n" + \
        "<b>Аккаунт</b>" + "\n" \
       '/account' + " - скажу, как изменить информацию о владельце аккаунта" + "\n" \
       '/return_account' + " - скажу, как восстановить доступ к аккаунту"


help = "Я могу помочь Вам решить некоторые вопросы." \
       + "\n\n" + \
       "Управлять мной Вы можете через следующие команды:" \
       + "\n\n" + \
       "<b>Оплата</b>" + "\n" \
       + '/pay' + " - скажу как оплатить" \
       + "\n\n" + \
       "<b>Домены</b>" + "\n" \
       '/change_admin' + " - скажу, как сменить администратора домена" \
       + "\n" + \
       '/domain_transfer' + " - скажу, как сделать технический или административный перенос домена" \
       + "\n" + \
       '/difference' + " - скажу, чем отличается технический перенос от административного" \
       + "\n" + \
       '/whois' + " - покажу информацию по домену" \
       + "\n\n" + \
       "<b>Аккаунт</b>" + "\n" \
       '/account' + " - скажу, как изменить информацию о владельце аккаунта" + "\n" \
       '/return_account' + " - скажу, как восстановить доступ к аккаунту"


whois = "Введите доменное имя. Например: <b>timeweb.com</b>"



pay = "Оплатить услуги возможно с помощью раздела панели управления аккаунтом \"Финансы и оплата\", " \
      "либо с помощью раздела \"Оплата\" на нашем сайте: <a href=\"http://timeweb.com/ru/#pay\">timeweb.com</a>, выбрав подходящий способ оплаты." \
      + "\n\n" + \
      "На нашем сайте Вы также сможете ознакомиться с видеоинструкцией по вопросу " \
      "<a href=\"http://timeweb.com/ru/help/pages/viewpage.action?pageId=4982785\">оплаты услуг</a> "


difference = "<b>Технический</b> перенос домена необходим, когда осуществляется перенос сайта " \
             "от одного хостинг-провайдера к другому" \
             + "\n\n" + \
             "После <b>административного</b> переноса домена на наш договор появится возможность продлевать домен(ы) через " \
             "панель управления аккаунтом." + \
             "\n" + \
             '/domain_transfer'


transfer = "<b>Технический</b> или <b>административный</b> перенос? (чтобы узнать в чем отличие нажмите /difference)" \
           + "\n" + \
           "В ответном ссобщении введите, пожалуйста, \"технический\" или \"административный\""


tehno = "Выполнить технический перенос доменного имени " \
        " к нам можно двумя способами: " + "\n\n" + \
        "1 способ. Указать на стороне держателя NS-серверов домена " \
        "в качестве А-записи IP-адрес сервера, на котором расположен аккаунт (IP-адрес можно узнать на главной " \
        "странице Панели управления аккаунтом, под заголовком \"Доступ по FTP\"). " \
        "Затем необходимо добавить домен в панель управления в разделе “Домены и поддомены”, " \
        "выбрав “Разместить на NS-серверах”." + "\n\n" + \
        "2 способ. Указать на стороне регистратора или текущего хостинг-провайдера домена NS-серверы Timeweb. " \
        "Затем необходимо добавить домен в панель управления в разделе “Домены и поддомены”, выбрав " \
        "“Разместить на NS-серверах“" + "\n\n" \
                                        "Наши NS-серверы:" + "\n" + \
        "ns1.timeweb.ru" + "\n" + \
        "ns2.timeweb.ru" + "\n" + \
        "ns3.timeweb.org" + "\n" + \
        "ns4.timeweb.org" + "\n\n" + \
        "IP наших ns-серверов:" + "\n" + \
        "ns1.timeweb.ru - 92.53.116.200" + "\n" + \
        "ns2.timeweb.ru - 92.53.98.100" + "\n" + \
        "ns3.timeweb.org - 92.53.116.26" + "\n" + \
        "ns4.timeweb.org - 92.53.98.42" + "\n\n" \
                                          "Также инструкция по техническому переносу представлена в нашем справочнике http://timeweb.com/ru/help/x/XoFC" \
        + "\n\n" + \
        "В случае необходимости, указать наши NS-серверы для домена мы можем за Вас. Для этого необходимо отправить " \
        "сообщение на почту info@timeweb.ru либо из " \
        "<a href=\"https://hosting.timeweb.ru/tickets\">Панели управления аккаунтом</a>" \
        " и предоставить логин и пароль от панели управления доменом на стороне регистратора, " \
        "а также точку входа в панель управления."



admin = "Введите, пожалуйста, в ответном сообщении доменную зону Вашего домена (например ru, com, pro и т.п.)"


ru = "Для переноса доменного имени в зонах .RU и .РФ под наше административное управление (к регистратору R01), " \
     "Вам необходимо выполнить следующие действия:" \
     + "\n\n" + \
     "1. Предоставить для домена <b>AuthInfo</b>-код (код переноса);" \
     "2. Сообщить текущему регистратору способ подтверждения переноса домена;" \
     "3. Создать персону администратора домена в панели управления аккаунтом в разделе \"Домены и поддомены\" " \
     + "\n\n" + \
     "4. Пополнить баланс аккаунта на сумму 89 руб. (стоимость трансфера);" \
     "5. Сообщить нам выбранный Вами способ подтверждения переноса (заявление, e-mail, sms)." \
     + "\n\n" + \
     "Ознакомиться с подробной инструкцией по административному переносу " \
     "домена Вы можете, пройдя по данной ссылке:" \
     "http://timeweb.com/ru/help/pages/viewpage.action?pageId=9240580" \
     + "\n\n" + \
     "Необходимо изучить инструкцию \"Перенос домена от другого регистратора на договор Timeweb в R01\"." \
     + "\n\n" + \
     "Также не забудьте добавить доменное имя в панель управления через раздел " \
     "\"Домены и поддомены\", опция \"Разместить домен на NS-серверах\", поскольку " \
     "автоматически он там не появится." \
     + "\n\n" + \
     "Остались вопросы? " \
     "Нажмите /help"


com = "Для смены регистратора на PDR Вам необходимо выполнить следующие действия:" \
      + "\n\n" + \
      "1. Снимите для домена запрет на смену регистратора \"clientTransferProhibited\" и получите " \
      "код авторизации реестра (secret key), обратившись к текущему регистратору или хостинг-провайдеру." \
      + "\n\n" + \
      "2. В панели управления аккаунтом в Timeweb создайте администратора, на данные которого будет перенесен домен." \
      + "\n\n" + \
      "3. Пополните баланс аккаунта в Timeweb на сумму, равную стоимости продления домена на 1 год - при переносе " \
      "доменное имя автоматически продлевается на 1 год. Сама процедура переноса (трансфера) " \
      "домена является бесплатной, поэтому кроме продления ничего дополнительно оплачивать не нужно." \
      + "\n\n" + \
      "Создайте обращение из раздела панели управления аккаунтом \"Служба поддержки\". " \
      "В обращении необходимо указать полученный код авторизации реестра (secret key) " \
      "и запрос на создание анкеты на договоре Timeweb в PDR." \
      + "\n\n" + \
      "После заказа переноса на административный e-mail домена будет отправлена ссылка, " \
      "по которой нужно пройти и подтвердить перенос доменного имени." \
      + "\n\n" + \
      "Трансфер, как правило, выполняется в течение 5-7 дней." \
      + "\n\n" + \
      "Остались вопросы? " \
      "Нажмите /help"


webnames = "К сожалению, административный перенос данного доменого имени на договор Timeweb невозможен." \
           + "\n\n" + \
           "Остались вопросы? " \
           "Нажмите /help"


change_adm = "Администратор домена - лицо (физическое или юридическое), на имя которого зарегистрирован домен." \
             + "\n\n" + \
             "При необходимости домен может быть передан от одного владельца другому. " \
             "Процедура смены администратора зависит от зоны, в которой зарегистрирован домен, " \
             "а также от регистратора, у которого доменное имя было зарегистрировано." \
             + "\n\n" + \
             "Подробная информация предоставлена в нашем " \
             "<a href=\"https://timeweb.com/ru/help/pages/viewpage.action?pageId=4358496\">Справочном центре</a>" \


own_account1 = "Любые изменения в профиле Вашего аккаунта Вы можете осуществлять самостоятельно (в том числе, " \
               "менять владельца аккаунта). Для внесения изменений Вам необходимо иметь доступ " \
               "к текущему контактному e-mail аккаунта. Узнать, как изменить данные Вы можете ознакомившись " \
               "с <a href=\"https://timeweb.com/ru/help/pages/viewpage.action?pageId=4358509\">данной инструкцией</a>" \
               + "\n\n" \
               + "В случае, если у Вас нет доступа к контактному e-mail, то для изменения данных напишите в нашу " \
                 "<a href=\"https://hosting.timeweb.ru/support/4/89\">Службу поддержки</a>"




own_account2 = "Кликните на логин в правом верхнем углу и перейдите в раздел \"Профиль аккаунта\":"


own_account3 = "Далее нажмите на ссылку \"Изменить данные\":"


own_account4 = "В новом окне укажите необходимые сведения и нажмите \"Сохранить, запросив код подтверждения\". " \
               "Код будет отправлен на контактный e-mail Вашего аккаунта."


own_account5 = "После введите полученный код в соответствующее поле и нажмите \"Сохранить\"." \
               + "\n\n" + \
               "<b>Примечание</b>" \
               + "\n" + \
               "В случае если Вы являетесь клиентом интегратора, для смены данных в профиле аккаунта необходимо " \
               "обратиться к интегратору."

were_password = "Для восстановления доступа в панель управления аккаунтом выполните следующие действия:" \
                + "\n\n" + \
                "1. Зайдите на <a href=\"https://hosting.timeweb.ru/login\">страницу авторизации</a>." \
                + "\n" + \
                "2. Нажмите на ссылку \"Восстановление пароля\"." \
                + "\n" + \
                "3. Введите логин аккаунта или доменное имя. Ссылка для восстановления доступа будет отправлена " \
                "на контактный e-mail, который был указан при регистрации аккаунта."




# <a href=\"https://hosting.timeweb.ru/login\">страницу авторизации</a>
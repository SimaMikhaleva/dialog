
define e = Character('Доктор', color="#c8ffc8", what_bold = True, what_italic = True)

label start:
    scene back with dissolve
    show prof_norm
    "Здравствуйте, что Вас беспокоит?"
    "Расскажите о Ваших симптомах"
    menu:
        "У Вас болит горло?"
        "Да":
            jump gorlobolit
        "Нет":
            jump gorlonebolit
    return

label gorlobolit:
    "Вы жалуетесь на больное горло. А теперь расскажите, есть ли у Вас есть покраснение гланд?"
    menu:
        "У Вас есть покраснение гланд?"
        "Да":
            jump krasnyeglandy
        "Нет":
            jump nekrasnyeglandy
return

label krasnyeglandy:
        "Вы так же заметили покраснение гланд. Скажите, а замечали ли Вы пробки в миндалинах?"
        menu:
            "Замечали ли Вы пробки в миндалинах?"
            "Да":
                jump estprobki
            "Нет":
                jump nekrasnyeglandy
return

label nekrasnyeglandy:
    "Похоже на фарингит"
return

label estprobki:
    "Задам такой вопрос..."
    menu:
        "Отмечаете ли Вы припухлость миндалин?"
        "Да":
            jump pripuhlost
        "Нет":
            jump nekrasnyeglandy
return

label pripuhlost:
    "Мне нужно еще совсем немного сведений о Вас"
    menu:
        "Беспокоит ли Вас болезненное глотание?"
        "Да":
            jump bolnoglotat
        "Нет":
            jump bolnoglotat
    return

label bolnoglotat:
    "Мне кажется, что у Вас ангина"
    return

label gorlonebolit:
    "Уже хорошо. Замечали ли Вы повышение температуры тела?"
    menu:
        "Температура повышена?"
        "Да":
            jump esttempa
        "Нет":
            jump nettempa
return

label esttempa:
    "Вопрос такой. Есть ли у Вас ощущение слабости?"
    menu:
        "Чувствуете ли Вы слабость?"
        "Да":
            jump estslabost
        "Нет":
            jump netslabosti
return

label estslabost:
    "А проблем с аппетитом у Вас нет?"
    menu:
        "Хороший ли у Вас аппетит?"
        "Да":
            jump horoshiyappetit
        "Нет":
            jump plohoyappetit
    return

label horoshiyappetit:
    "Возникает подозрение на ожог, обморожение или внутреннее воспаление"
    return

label plohoyappetit:
    "Возникает подозрение на ГРИПП или ОРВИ"
    return


label netslabosti:
    "А что насчет обоняния?"
    menu:
        "Ваше обоняние в норме?"
        "Да":
            jump normobonyanie
        "Нет":
            jump plohoeobonyanie
    return

label normobonyanie:
    "Думаю, что у Вас аллергия"
    return

label plohoeobonyanie:
    "Думаю, что у Вас простуда и снижен иммунитет. Не усугубите, пожалуйста! "
    return

label nettempa:
    "Отлично, а теперь расскажите..."
    menu:
        "Нет ли у Вас насморка?"
        "Да":
            jump estnasmork
        "Нет":
            jump netnasmorka
    return

label estnasmork:
    "Попрошу Вас оценить, как давно появился насморк"
    menu:
        "Как давно у Вас насморк?"
        "Продолжительное время":
            jump netslabosti
        "Недавно возникший":
            jump netslabosti
    return

label netnasmorka:
    "Это замечательно. Может головная боль Вас беспокоит?"
    menu:
        "Беспокоит ли Вас головная боль?"
        "Да":
            jump golovabolit
        "Нет":
            jump golovanebolit
    return

label golovabolit:
    "Расскажите, а давно ли у Вас болит голова?"
    menu:
        "Как давно у Вас болит голова?"
        "Давно":
            jump davnogolova
        "Недавно заболела и ненадолго":
            jump nedavnogolova
    return

label davnogolova:
    "Расскажите, пожалуйста, про характер боли"
    menu:
        "Оцените характер боли?"
        "Пульсирующая":
            jump pulse
        "Постоянная":
            jump postoyanno
    return

label pulse:
    "Думаю, что у Вас мигрень"
    return

label postoyanno:
    "Возможен и менингит"
    return

label nedavnogolova:
    "Подозреваю, что Вы переутомились"
    return

label golovanebolit:
    "Прекрасно! Может у Вас заложен нос?"
    menu:
        "Заложен ли у Вас нос?"
        "Да":
            jump noszalojen
        "Нет":
            jump nosnezalojen
    return

label noszalojen:
    "Хочу попросить Вас оценить длительность заложенности носа"
    menu:
        "Как долго у Вас заложен нос?"
        "Долго":
            jump noszalojendolgo
        "Недолго":
            jump noszalojendolgo
return

label noszalojendolgo:
    "Расскажите, чихаете ли Вы?"
    menu:
        "Вы чихаете?"
        "Да":
            jump chihay
        "Нет":
            jump normobonyanie
return

label chihay:
    "Возникает мысль, что у Вас ринит"
    return

label nosnezalojen:
    "А что насчет кашля? Может он Вас мучает?"
    menu:
        "Вы кашляете?"
        "Да":
            jump estkashel
        "Нет":
            jump netkaslya
return

label estkashel:
    "Расскажите, а как давно у Вас появился кашель?"
    menu:
        "Как давно Вы кашляете?"
        "Давно":
            jump davnokashel
        "Недавно":
            jump plohoeobonyanie
    return

label davnokashel:
    "А теперь расскажите о характере Вашего кашля"
    menu:
        "Какой у Вас кашель - сухой или влажный?"
        "Сухой":
            jump plohoyappetit
        "Влажный":
            jump netslabosti
    return

label netkaslya:
    "Поздравляю Вас, Вы здоровы!!!"
    return

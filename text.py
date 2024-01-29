GREETING = "<b>Привет, я бот, для удобного просмотра афиши любимых Чебоксар :)</b>\n\
           /today - афиша на сегодня /tommorow - на завтра"


def transform_text(lsts):
    TRANSFORM_TEXT = ""
    for lst in lsts:
        TRANSFORM_TEXT += " ".join(lst) + "\n" + "----------" + "\n"
    return TRANSFORM_TEXT

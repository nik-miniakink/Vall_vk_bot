from peewee import *
import sec_and_pass as p

# Connect to a Postgres database.
pg_db = PostgresqlDatabase(p.bd, user=p.user, password=p.password,
                           host=p.host, port=p.port)


class BaseModel(Model):
    class Meta:
        database = pg_db


class AmigosBase(BaseModel):
    """
    Информация об участниках
    """
    id = PrimaryKeyField(null=False)
    vk_id = IntegerField(null=False)
    name = CharField(max_length=20, null=False)  # уточнить имя или фамилия и развести по колонкам
    nickname = CharField(max_length=10, null=False)  # переименовал переменную и возможно стоит этот столбец ключем?
    rang = CharField(max_length=10, null=False)  # может дописать таблицу значений поля ранг? и сделать чисто выбирать?

    class Meta:
        db_table = "amigos_base"
        order_by = ('name',)


class Games(BaseModel):
    """
    Информация об играх будущих и прошедших
    """
    id = PrimaryKeyField(null=False)  # удалить
    date = TextField(null=False)
    city = CharField(null=False, max_length=15)  # переименовал переменную
    title = CharField(null=False, max_length=50)
    organizer = CharField(null=False, max_length=20)  # переименовал переменную

    class Meta:
        db_table = 'games'
        order_by = ('title',)


class AmigosInfo(BaseModel):
    """
    Подробная инфорация об участниках   #совместьь с таблицей Amigos
     """
    id = PrimaryKeyField(null=False)
    nic = CharField(max_length=10, null=False)  # удалить повторяющуюся строку
    birtday = DateField(null=False)  # переименовал переменную.
    phone = CharField(null=False, max_length=25)  # переименовал переменную
    address = TextField(null=False)

    class Meta:
        db_table = 'amigos_info'
        order_by = ('nic',)
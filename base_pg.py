from peewee import *
import sec_and_pass as p

# Connect to a Postgres database.
pg_db = PostgresqlDatabase(p.bd, user=p.user, password=p.password,
                           host=p.host, port=p.port)

class BaseModel(Model):
    class Meta:
        database = pg_db


class AmigosBase(BaseModel):
    id = PrimaryKeyField(null=False)
    vk_id = IntegerField(null=False)
    name = CharField(max_length=20, null=False)
    nic = CharField(max_length=10, null=False)
    rang = CharField(max_length=10, null=False)

    class Meta:
        db_table = "amigos_base"
        order_by = ('name',)

class Games(BaseModel):
    id = PrimaryKeyField(null=False)
    date = TextField(null=False)
    citi = CharField(null=False, max_length=15)
    title = CharField(null=False, max_length=50)
    orgs = CharField(null=False, max_length=20)

    class Meta:
        db_table = 'games'
        order_by = ('title',)



class AmigosInfo(BaseModel):
    id = PrimaryKeyField(null=False)
    nic = CharField(max_length=10, null=False)
    date_bird = DateField(null=False)
    tel = CharField(null=False, max_length=25)
    address = TextField(null=False)

    class Meta:
        db_table = 'amigos_info'
        order_by = ('nic',)
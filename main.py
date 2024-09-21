from sqlalchemy.orm import mapped_column,sessionmaker, DeclarativeBase, Mapped
from sqlalchemy import create_engine

from datetime import datetime
from sqlalchemy import String
# engine = create_engine("sqlite:///my_db.db", echo=True)
# Session = sessionmaker(engine)


# class Base(DeclarativeBase):
#     id: Mapped [int]= mapped_column(primary_key=True)

# def up():
#     Base.metadata.create_all(engine)


# def down():
#     Base.metadata.drop_all(engine)



# up()


# class WebsiteUser(Base):
#     __tablename__ = "users"

#     password: Mapped[str]
#     login: Mapped[str]
    
# password = input("Password please burger cheese: ")
# login = input("Login plis: ")
# with Session.begin() as session:
#     websiteuser = WebsiteUser(password=password, login=login)
#     session.add(websiteuser)


engine = create_engine("sqlite:///my.sql", echo=True)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


#OUR MODELS

class RioFitnessClubVisitor(Base):
    __tablename__ = "visitors"
    number : Mapped[str]
    name : Mapped[str]
    bought_date : Mapped[datetime]
    expiring_date : Mapped[str]
    is_human : Mapped[bool]

Base.metadata.create_all(engine)
Session = sessionmaker(engine)

number = input("Input your number: ")
if number.startswith("+380") and len(number) == 13 and number[1:14].isdigit():
    pass
else:
    print("Error")
    raise ValueError("False number")
name = input("Input name: ")
bought_date = datetime.now()
expiring_date = bought_date.replace(year=bought_date.year+1)
sex = input("Input your sex \n Male or Female: ")
if sex == "Male":
    is_human = True
else:
    is_human = False


print(name, number, bought_date, expiring_date, is_human)
with Session.begin() as session:
    event = RioFitnessClubVisitor(number=number, name=name, bought_date=bought_date, expiring_date=expiring_date, is_human=is_human)
    session.add(event)
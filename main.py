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

Base.metadata.create_all(engine)
Session = sessionmaker(engine)

number = input("Input your number: ")
if number.startswith("+380") and len(number) == 13 and number[1:14].isdigit():
    pass
else:
    print("Error")
    raise ValueError("False number")
name = input("Input name: ")

print(name, number)
with Session.begin() as session:
    event = RioFitnessClubVisitor(number=number, name=name)
    session.add(event)
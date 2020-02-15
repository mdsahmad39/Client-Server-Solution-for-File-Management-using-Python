"""Handles user registration and login along with requests from server for executing commands
"""
import os

from .user_functions import UserCommands, AdminCommands

MAIN_DIRECTORY = os.getcwd()


def ad_min():
    """
    A simple function which reads admin.txt file containing admin credentials
    which resides in main directory.

    Returns:
        Dictionary by taking admin username as keys and password as its respective value.
        If file is empty returns empty dictionary
    """
    if os.path.getsize(f"{MAIN_DIRECTORY}\\admin.txt") == 0:
        return {}
    else:
        with open(f"{MAIN_DIRECTORY}\\admin.txt", 'r') as file:
            data = file.read().splitlines()
            admin1 = {}
            for _user in data:
                use_r = _user.split(" ")
                name = use_r[0]
                admin1[name] = use_r[1]
        assert admin1 is not None
        return admin1


def u_ser():
    """
    A simple function which reads user.txt file containing user credentials
    which resides in main directory.

    Returns:
        Dictionary by taking user username as keys and password as its respective value.
        If file is empty returns empty dictionary
    """
    if os.path.getsize(f"{MAIN_DIRECTORY}\\user.txt") == 0:
        return {}
    else:
        with open(f"{MAIN_DIRECTORY}\\user.txt", 'r') as file:
            data = file.read().splitlines()
            user1 = {}
            for user_ in data:
                use_r = user_.split(" ")
                name = use_r[0]
                user1[name] = use_r[1]
                file.close()
        assert user1 is not None
        return user1


def login_users():
    """
    A simple function which reads login_users.txt file containing
    username's of currently logged in users

    Returns:
        A list containing username's of logged in users.
        If there are no active users returns empty list
    """
    if os.path.getsize(f"{MAIN_DIRECTORY}\\login_users.txt") == 0:
        return []
    else:
        with open(f"{MAIN_DIRECTORY}\\login_users.txt", 'r') as credentials:
            user_log = [line.strip() for line in credentials]
            assert user_log is not None
            return user_log


def merge_dict():
    """
    A simple function which combines dictionaries containing
    admin credentials and user credentials.

    Returns:
        A dictionary containing credentials of both admin and user,
        with username as key and and password as its respective value
    """
    return {**ad_min(), **u_ser()}


class UserFunction:
    """
    A class used to register and login different users

    ...

    Attributes:
    -----------------------------
        username : string
            stores username
        password : string
            stores password
        privileges : string
            stores privilege

    Methods:
    -----------------------------
        __init__(self):
            Initialises all the attributes

        user_reg(self, username, password, privileges):
            registers the new user with respective privilege.

        user_login(self, username, password):
            user gets login into their respective account.

        quit(self):
            function used to quit from current session.

        commands(self):
            function returns the commands and its format

    """

    def __init__(self):
        """
        Initialising all the attributes
        """
        self.username = ''
        self.password = ''
        self.privileges = ''

    def user_reg(self, username, password, privileges):
        """
        This function lets the user to register new account. If other user
        already exists with same name, the user can't register. It creates own
        working directory for each user with their respective username. It also
        checks if there is any directory with username during registration, and
        asks new user to give another name.
        Args:
            username: 'user choice'
            password: 'user choice'
            privileges: admin or user

        Returns: string
            Acknowledgement if user account is created or not.
        """
        files = os.listdir(MAIN_DIRECTORY)
        if username in merge_dict().keys():
            return "\nThe name is already taken, please choose other name"

        elif username in files:
            return "\nYou can't choose this name, please select another name"

        elif privileges == 'admin':
            if ad_min() == {}:
                login = f"{username} {password}"
                old = open(f"{MAIN_DIRECTORY}\\admin.txt", 'w')
                old.write(f'{login}')
                old.close()
            else:
                login = f"{username} {password}"
                old = open(f"{MAIN_DIRECTORY}\\admin.txt", 'a+')
                old.write(f'\n{login}')
                old.close()
            folder1 = f"{MAIN_DIRECTORY}/{username}"
            os.makedirs(folder1)
            return "\nYou're account is successfully created"

        elif privileges == 'user':
            if u_ser() == {}:
                login = f"{username} {password}"
                old = open(f"{MAIN_DIRECTORY}\\user.txt", 'w')
                old.write(f'{login}')
                old.close()
            else:
                login = f"{username} {password}"
                old = open(f"{MAIN_DIRECTORY}\\user.txt", 'a+')
                old.writelines(f'\n{login}')
                old.close()
            folder1 = f"{MAIN_DIRECTORY}/{username}"
            os.makedirs(folder1)
            return "\nYou're account is successfully created"
        else:
            return "Please use proper privilege, either admin or user"

    def user_login(self, username, password):
        """

        This function let's the user to login into their respective accounts.
        It recalls the admin and user credentials which are saved as dictionaries
        to check user password and it also saves username in a text file to not allow
        current user in any other session
        Args:
            username: username
            password: password

        Returns: string
            Acknowledgement of login status

        """
        if username in merge_dict().keys():
            dict1 = merge_dict()
            if dict1[username] != password:
                return "\nThe password is wrong, please type again"
            else:
                if os.path.getsize(f"{MAIN_DIRECTORY}\\login_users.txt") == 0:
                    write = open(f"{MAIN_DIRECTORY}\\login_users.txt", 'a+')
                    write.writelines(f"{self.username}")
                    write.close()
                else:
                    write = open(f"{MAIN_DIRECTORY}\\login_users.txt", 'a+')
                    write.writelines(f"\n{self.username}")
                    write.close()
                return "\nYou're successfully logged in"

    def quit(self):
        """

        Function which removes username from current login session and
        closes the current working directory and stops
        the current login session

        Returns: string
            Acknowledgement of logging out of current session

        """
        global X
        cred = open(f"{MAIN_DIRECTORY}\\login_users.txt", 'r')
        credential_s = cred.readlines()
        for i in range(len(credential_s)):
            if self.username in credential_s[i]:
                X = i
        cred.close()
        credential = open(f"{MAIN_DIRECTORY}\\login_users.txt", 'w')
        for i in range(len(credential_s)):
            if X != i:
                credential.writelines(credential_s[i])
        credential.close()
        return "You're successfully logged out from your current session"

    def commands(self):
        """

        Simple function which contains all the commands along with the format

        Returns: string
            commands with its usage and format

        """
        return '''The commands which you can use are given below:

Make sure you type command first and then the input with space among each of them        
format--> <command> <...> <...> ...,
example--> register user pass admin (This is for registering new account)

Commands            Purpose                                                 Format
------------------------------------------------------------------------------------------------------------------------
register       --> For registering new account,                 format--> <username> <password> <privileges>
login          --> For login,                                   format--> <username> <password>

The following commands can only be used when your logged in your account

create_folder  --> For creating new folder in current           format--> <folder name>
                       working directory      
change_folder  -->  The folder name you want to work on         format--> <folder name>
                       or '..' To walk back to previous folder
list           --> Print all files and folders in the           format--> <list>
                       current working directory 
read_file      --> To read data from the file                   format--> <file name>
write_file     --> To write data in the file                    format--> <file name> <data> 
quit           --> To logout the from current session           format--> <quit>

The following commands can only be used by admin users while they are logged in their account

delete         --> To delete account from database              format--> <username> <password>
                                                                'the password must be of admin account'
                  
'''


class Commands(UserFunction):
    """

    Commands class which inherits from UserFunction class

    Attributes:
    -------------------------------------------
        ip : list
        contains details of connected user
    Methods:
    -------------------------------------------
        __init__(self, ip):
            initialising all Commands class attributes
        execute(self, data):
            executes the called function from client and returns response accordingly

    """

    def __init__(self, ip_address):
        """
        Initialising all the attributes
        Args:
            ip : list
            contains data of client. So that the response is send only to respective client
        """

        super().__init__()
        self.ip_address = ip_address

    def execute(self, data):
        """
        Executes commands with proper input. Contains if-else loops to
        check and to return proper response to client
        Args:
            data: string
                data is stripped into respective command format and mapped to respective categories.

        Returns: string
            If input checks-out to be proper, respective function is called and the data is analyzed
            and proper message is sent to client.

        """
        statement = data.rstrip("\n")
        com = statement.split(" ")[0]
        commands = ('commands', 'register', 'quit', 'login', 'list', 'change_folder',
                    'create_folder', 'read_file', 'write_file', 'delete')
        if com.lower() not in commands:
            return '''Please enter valid command
To know what commands you can use...Please type "COMMANDS"'''
        elif com.lower() == 'commands':
            return self.commands()
        elif com.lower() == "register":
            if len(statement.split(" ")) == 4 and self.username == '':
                return self.user_reg(statement.split(" ")[1],
                                     statement.split(" ")[2],
                                     statement.split(" ")[3])
            return "Make sure you have typed correct command format and your not logged in"
        elif com.lower() == "login":
            if len(statement.split(" ")) == 3 and self.username == '':
                if statement.split(" ")[1] in login_users():
                    return "The user is logged in another session"
                else:
                    if statement.split(" ")[1] not in merge_dict().keys():
                        return "There  is no user with given name"
                    else:
                        self.username = statement.split(" ")[1]
                        self.password = statement.split(" ")[2]
                        files = os.listdir(MAIN_DIRECTORY)
                        if self.username not in files:
                            folder = f"{MAIN_DIRECTORY}/{self.username}"
                            os.makedirs(folder)
                        else:
                            pass
                        os.chdir(f"{MAIN_DIRECTORY}/{self.username}")
                        return self.user_login(statement.split(" ")[1],
                                               statement.split(" ")[2])
            return "Make sure you have typed correct command and your not logged in"
        else:
            object_1 = UserCommands(self.username, self.password)
            object_2 = AdminCommands(self.username, self.password)
            if com.lower() == "list":
                return str(object_1.list())
            elif com.lower() == "change_folder":
                return object_1.change_folder(statement.split(" ")[1])
            elif com.lower() == "read_file":
                return object_1.read_file(statement.split(" ")[1])
            elif com.lower() == "write_file":
                return object_1.write_file(statement.split(" ")[1], statement.split(" ")[2:])
            elif com.lower() == "create_folder":
                return object_1.create_folder(statement.split(" ")[1])
            elif com.lower() == "delete":
                return object_2.delete_user(statement.split(" ")[1], statement.split(" ")[2])
            elif com.lower() == 'quit':
                self.username = ''
                return self.quit()

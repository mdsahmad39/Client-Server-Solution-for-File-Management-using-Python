"""Handles various User commands"""
import os
import shutil

from Main_Directory import user_handling


class UserCommands:
    """
    This class contains the functions(commands) which are performed by users

    ...

    Attributes:
    ------------------------------------------
        username : string
            stores username
        password : string
            stores password
        current_directory : string
            stores Current working Directory
        start_point : integer
            this is used to read file from certain position which gets updated every time
    Methods:
    --------------------------------------------
        __init__(self):
            Initialises all the attributes

        create_folder(self, folder_name):
            creates a new folder

        change_folder(self, folder_name):
            changes current working folder

        write_file(self, file_name, data):
            edits or creates file with the given input data

        read_file(self, file_name):
            contains logic for reading from files

        list(self):
            list the file in the current directory


        """

    def __init__(self, username, password):
        """ Initialising the UserCommands class
        Parameters:
        --------------------------------------------
        start_point : integer
            this is used to read file
        username : string
            stores username
        password : string
            stores password
        current_directory : string
            If current directory is none, it is created as list and
            the files are stored in it for future calling
        """
        self.start_point = 0
        self.username = username
        self.password = password

    def create_folder(self, folder_name):
        """Creating a folder
        Parameters:
                folder_name : string
                    name of the folder to create in current working directory
        """
        if self.username != "":
            try:
                path = os.getcwd()
                folder = f"{path}/{folder_name}"
                os.makedirs(folder)
                return "\nFolder created successfully"
            except FileExistsError:
                return "\n The folder cant be created as the name already exists"
        return "make sure your logged in to use this command"

    def change_folder(self, folder_name):
        """Changes the folder
                Parameters:
                    folder_name : string
                        name of the folder you want to work on
        """
        if self.username != '':
            try:
                path = os.getcwd()
                root_directory = user_handling.MAIN_DIRECTORY
                if folder_name == '..':
                    if self.username in user_handling.ad_min().keys():
                        if path == root_directory:
                            return "You can't go back further"
                        else:
                            os.chdir('../')
                            return "Working directory changed successfully"
                    else:
                        path1 = f"{user_handling.MAIN_DIRECTORY}\\{self.username}"
                        if path == path1:
                            return "You can't go back further"
                        else:
                            os.chdir('../')
                            return "Working directory changed successfully"
                else:
                    os.chdir(f"{path}\\{folder_name}")
                    assert folder_name is not None
                    return "Working directory changed successfully"
            except AssertionError:
                return "Please try again"
            except FileNotFoundError:
                return "There is no such folder in current working directory"
            except FileExistsError:
                return "There is no such folder in current working directory"
        return "make sure your logged in to use this command"

    def write_file(self, file_name, data):
        """Writes client input data into the file
        Parameters:
            file_name : string
                stores the file name
            data : string
                stores the data in the file, if there is no such file
                in current working directory it'll be created
        """
        if self.username != '':
            path = os.getcwd()
            path1 = os.listdir(path)
            if f'{file_name}.txt' not in path1:
                file = open(f'{file_name}.txt', 'w+')
                file.write(" ".join(data) + "\n")
                file.close()
                return "\nFile Created With Input Data Successfully"
            else:
                file = open(f"{file_name}.txt", "a+")
                file.write(" ".join(data) + "\n")
                file.close()
                return "\nFile Edited Successfully"
        return "make sure your logged in to use this command"

    def read_file(self, file_name):
        """
        Reads the values from the file and returns exactly 100 character.
        This function also updates the start_point attribute, to return
        next 100 characters for next call
        Parameters:
            file_name : string
                file name that has to be read
        """
        if self.username != '':
            try:
                check = open(f'{file_name}.txt', 'r')
                check.close()
            except FileExistsError:
                return "There is no such file in current working directory"
            except FileNotFoundError:
                return "There is no such file in current working directory"
            else:
                start = self.start_point + 100
                file = open(f'{file_name}.txt', 'r')
                data = file.read()
                num_char = len(data)
                file.close()
                if num_char > start:
                    file1 = open(f'{file_name}.txt', 'r')
                    data = file1.read(start)
                    if start == num_char:
                        file1.close()
                return data
        return "make sure your logged in to use this command"

    def list(self):
        """
        Files are listed from current working directory
        """
        if self.username != '':
            try:
                path = os.getcwd()
                files = os.listdir(path)
                if not files:
                    return "The current directory is empty"
                else:
                    assert files is not None
                    return files
            except AssertionError:
                return "Please try again"
        return "make sure your logged in to use this command"


class AdminCommands(UserCommands):
    """AdminCommands class is created which inherits from UserCommands

    Attributes:
    -------------------------------------------------------
        start_point : integer
            stores the integer value to start reading from certain position
    Methods:
    -------------------------------------------------------
        __init__(self):
            Initialises all the attributes

        delete_user(self, username):
            deletes the user and all the contents of the folder
    """

    def __init__(self, username, password):
        """Initialising variables

        username : string
            username of current user
        password: password
            password of current user
        start_point : string
            this is used to read files
        """
        super().__init__(username, password)
        self.start_point = 0

    def delete_user(self, user, password):
        """
        This method is only available to users with admin privileges.
        It automatically checks the password of admin to allow this function to run.
        This methods deletes the user and user directory.

        Parameters:
            user : string
                name of the user to delete from database
            password : string
                password of the admin user
        """
        if self.username == '':
            return "make sure your logged in to use this command"
        elif self.username not in user_handling.ad_min().keys():
            return "You are not authorised to use this command"
        elif (user == self.username) or (user in user_handling.ad_min().keys()):
            return "You can't delete yourselves, neither other admin user"
        elif password != self.password:
            return "\n The password entered is wrong, make sure its your password"
        elif user in user_handling.u_ser().keys():
            path = user_handling.MAIN_DIRECTORY
            files = os.listdir(path)
            if user in files:
                user_file = f"{user_handling.MAIN_DIRECTORY}/{user}"
                shutil.rmtree(user_file)
            with open(f"{user_handling.MAIN_DIRECTORY}\\user.txt", 'r') as file:
                data = file.read().splitlines()
                user1 = {}
                for user_ in data:
                    use_r = user_.split(" ")
                    name = use_r[0]
                    user1[name] = use_r[1]
            d_ata = open(f"{user_handling.MAIN_DIRECTORY}\\user.txt", 'w')
            for i in user1.keys():
                if user != i:
                    d = f"{i} {user1[i]}\n"
                    d_ata.writelines(d)
                    print(i)
            return "\n the user is deleted from database"
        else:
            return"\n the user does'nt exist"

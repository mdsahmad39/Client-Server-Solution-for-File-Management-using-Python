import unittest
import sys
import os

from Main_Directory.user_handling import Commands, UserFunction

PATH = os.getcwd()


class UserHandlingTestingStepOne(unittest.TestCase):
    """Handles the tests for User Register and User Login"""

    def test_user_reg(self):
        """
        This test will create User instance with different input
        formats.
        Two users will be tried to register.
            One will be with existing username
            One will be with wrong privilege
        """
        user = Commands("127.0.0.1")
        expected_result = ["\nThe name is already taken, please choose other name",
                           "Please use proper privilege, either admin or user"
                           ]
        results = []
        test1 = "register user password admin"
        test2 = "register user1 password admins"
        tests = [test1, test2]
        for test in tests:
            results.append(user.execute(test))
        self.assertListEqual(results, expected_result)

    def test_user_login(self):
        """
        This test will create User instance with different input 
        formats.
        Three users will be tried to login.
            One will be with wrong username
            One will be in correct format
            One will be in correct format but user is already logged in
        """
        file = open(f"{PATH}//login_users.txt", 'w')
        file.close()
        user = Commands("127.0.0.1")
        expected_result = ["There  is no user with given name", "\nYou're successfully logged in",
                           "Make sure you have typed correct command and your not logged in"
                           ]
        results = []
        test1 = "login user1 password"
        test2 = "login user password"
        test3 = "login user password"
        tests = [test1, test2, test3]
        for test in tests:
            results.append(user.execute(test))
        self.assertListEqual(results, expected_result)


class UserHandlingTestingStepTwo(unittest.TestCase):
    """Handles the tests for Creating folder, Changing folder and Delete folder"""

    def test_create_folder(self):
        """
        This test will create User instance with different input
        formats.
        Three folders are tried to be created.
            One will be without login of user
            One will be with folder which already exists in current directory
            One will be with folder name which doesnt exists will be created.
        """
        file = open(f"{PATH}//login_users.txt", 'w')
        file.close()
        user = Commands("127.0.0.1")
        expected_result = ["make sure your logged in to use this command",
                           "\n The folder cant be created as the name already exists",
                           "\nFolder created successfully"
                           ]
        results = []
        test1 = "create_folder folder"
        results.append(user.execute(test1))
        login = "login user password"
        user.execute(login)
        test2 = "create_folder folder"
        test3 = "create_folder folder1"
        tests = [test2, test3]
        for test in tests:
            results.append(user.execute(test))
        self.assertListEqual(results, expected_result)

    def test_change_folder(self):
        """
        This test will create User instance with different input
        formats.
        Three times directory is tried to be changed.
            One will be without login of user
            One will be with folder which doesnt exists in current directory
            One will be with folder name which exists, directory will be changed.
        """
        file = open(f"{PATH}//login_users.txt", 'w')
        file.close()
        user = Commands("127.0.0.1")
        expected_result = ["make sure your logged in to use this command",
                           "There is no such folder in current working directory",
                           "There is no such folder in current working directory"
                           ]
        results = []
        test1 = "change_folder folder"
        results.append(user.execute(test1))
        login = "login user password"
        user.execute(login)
        test2 = "change_folder folder3"
        test3 = "change_folder folder1"
        tests = [test2, test3]
        for test in tests:
            results.append(user.execute(test))
        self.assertListEqual(results, expected_result)


class UserHandlingTestingStepThree(unittest.TestCase):
    """Handles the tests for Writing text file and Reading Text file"""
    def test_write_file(self):
        """
        This test will create User instance with different input
        formats.
        Three times file is tried to be manipulated.
            One will be without login of user
            One will be with filename which doesnt exists, so it'll be created in current directory and data is added
            One will be with filename which exists, data is appended to it.
        """
        file = open(f"{PATH}//login_users.txt", 'w')
        file.close()
        user = Commands("127.0.0.1")
        expected_result = ["make sure your logged in to use this command",
                           "\nFile Created With Input Data Successfully",
                           "\nFile Edited Successfully"
                           ]
        results = []
        test1 = "write_file file"
        results.append(user.execute(test1))
        login = "login user password"
        user.execute(login)
        test2 = "write_file file This is new file"
        test3 = "write_file file This is new data to existing file"
        tests = [test2, test3]
        for test in tests:
            results.append(user.execute(test))
        self.assertListEqual(results, expected_result)

    def test_read_file(self):
        """
        This test will create User instance with different input
        formats.
        Two times file is tried to be read.
            One will be without login of user
            One will be with filename which doesnt exists in current directory
        """
        file = open(f"{PATH}//login_users.txt", 'w')
        file.close()
        user = Commands("127.0.0.1")
        expected_result = ["make sure your logged in to use this command",
                           "There is no such file in current working directory"
                           ]
        results = []
        test1 = "read_file file"
        results.append(user.execute(test1))
        login = "login user password"
        user.execute(login)
        test2 = "read_file file1"
        results.append(user.execute(test2))
        self.assertListEqual(results, expected_result)


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)

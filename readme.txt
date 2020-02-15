A simplified client-server solution for file management

This zip file contains two folders. Client_Code folder contains client code which can be used by any number of cllient's and 
in Main_Directory, server code's and files which are necessary for implementing this program are present. Please read further how to structure them.

In order to implement this program the server code(server_run, user_functions, user_handling) along 
with three text files (login_users.txt, user.txt, admin.txt) must reside in root directory.
For better implementation make sure that there is no other content in that directory while copying.

This is a simple client server program in which server accepts requests from any number of clients such as user registration, 
user login, create folder, change directory from one folder to another, read text file, write text file, print list of files in current working directory, 
commands in which all the commands are printed which can be used by client and finally quit to logout from their current logged in session.

The user can register either in admin privilege or normal user privilege.
Admin privilege users can delete normal users as well as modify data of normal users too.

The admin user have a special command delete. In which they can delete normal user if they know exact username of their's.

The Root Directory is divided into two categories such as the admin privilege users have 
access to all directories of normal users too. Whereas the normal user doesn't.

Also please go through readme.txt present in Tests folder, if you are trying to run tests for this client-server solution for file management.
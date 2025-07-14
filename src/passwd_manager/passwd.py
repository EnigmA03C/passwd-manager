import yaml
import sys
from data.passwd import passwd
import logging
log = logging.getLogger(__name__)

def main(arguments: list):
    if arguments[0] == "help":
        print("""
            Welcome to the help page of passwd-manager!
            
            if you want to insert a new password in the database all you have to do is excecute this script
            with the 'create' command as follows in the example:
            
            python passwd.py create service email|username password
            
            if you instead want to recover a password that is already within the database
            all you have to do is use the 'get' command with the service you want the password of:
            
            python passwd get service
            
            Or you can delete using:
            
            passwd delete service
            
            disclaimer: inserting the same service twice using the create function will delete the previous record
            and substitute it with the new one.
            """)
    elif arguments[0] == "create":
        if arguments[1] and arguments[2] and arguments[3] is not None:
            passwd.create(arguments[1], arguments[2], arguments[3])
        else:
            print("There are missing arguments, make sure you inserted service, mail and password correctly.")
            exit(0)
    elif arguments[0] == "get":
        credentials = passwd.read()[arguments[1]]
        print(f"""
              The mail/username is: {credentials[0]}
              and the password is: {credentials[1]}
              """)
        
    else:
        print("Wrong argument error, you need to use create or get, use the command 'help' to see the help page.")


if __name__ == "__main__":
    arguments: list = sys.argv[1:]
    main(arguments)

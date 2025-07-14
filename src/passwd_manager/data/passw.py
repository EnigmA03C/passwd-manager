import yaml
import logging
log = logging.getLogger(__name__)
import sys

class Password():
    passwd_path = "src\\passw_manager\\data\\passw.yml"
    def __init__(self) -> None:
        self.data: dict = {}
        try:
            with open(self.passwd_path, "r") as passw_file:
                log.info("reading password file.")
                self.data: dict = yaml.safe_load(passw_file)
                log.info("password file loaded correctly")
        except FileNotFoundError:
            log.critical(f"Password file was not found in {self.passwd_path}")
            sys.exit(1)
        except yaml.YAMLError as e:
            log.critical(f"A problem occurred with the password file: {e}")
            sys.exit(1)
        
    def create(self, service: str = "", user: str = "", passwd: str = "") -> None:
        if self.data is None:
            self.data = {service: [user, passwd]}
        else:
            self.data.update({service: [user, passwd]})
        self.save()
    
    def read(self) -> dict:
        return self.data # type: ignore
    
    def save(self):
        try:
            with open(self.passwd_path, "w") as passw_file:
                yaml.dump(self.data, passw_file, default_flow_style=False)
                log.info("password file saved successfully")
        except FileNotFoundError:
            log.critical("Password file was not found!")
            sys.exit(1)
        except yaml.YAMLError as e:
            log.critical(f"A problem occurred with the password file: {e}")
            sys.exit(1)
    
    def delete(self):
        pass

passwd = Password()
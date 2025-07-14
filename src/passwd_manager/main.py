import yaml
from data.passw import passwd
import logging
log = logging.getLogger(__name__)

def main():
    passwd.create("testservice", "test-mail|name", "test-passowrd")
    passwd.read()


if __name__ == "__main__":
    main()

# this is main.py file for the Python with AI Project

# import modules

import os
import sys
import math
from datetime import datetime
from core.calculator import Calculator
from core.user import user_login
from utils.helpers import log_info
from config.settings import Database_config, user_profiles






# Declare variables

# reading data from config folder
valid_user = user_login("user1", "password123")
log_info(f"User user1{valid_user} logged in successfully.")
user_profile = user_profiles.get("user1")
log_info(f"User profile: {user_profile}")

# loading environment variables
  





# main function ()
#calling the modules and functions in sequence (sequence of business logic/modules/functions/class or objects)

def main():
    log_info("Starting the Python with AI Project...")
    # Use Calculator as a callable operation function
    calc = Calculator
    result = Calculator(5, 3, ["add"])
    log_info(f"Addition result: {result}")
    result = Calculator(10, 4, ["subtract"])
    log_info(f"Subtraction result: {result}")
    result = Calculator(6, 7, ["multiply"])
    log_info(f"Multiplication result: {result}")
    result = Calculator(20, 5, ["divide"])
    log_info(f"Division result: {result}")
    log_info("Python with AI Project completed successfully.")

# call the main function
if __name__ == '__main__':
    main()
    

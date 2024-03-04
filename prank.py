import os
import random

if random.randint(1, 6) == 6: # Choose Random Number which i give 1,6 if the algo choose number 6 it will delete this prank.py file  
    try:
        os.remove(r"C:\PYTHON\Python-Project\prank.py")
        print("File removed successfully.")
    except FileNotFoundError:
        print(f"File not found: Error 404")
    except Exception as e:
        print(f"An error occurred: {e}")

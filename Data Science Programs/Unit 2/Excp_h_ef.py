try: 
    a=10/0 
    print(a) 
except Exception as e: 
    print(e)  
else: 
    print("No Error occured") 
finally: 
    print("Program Completed!")
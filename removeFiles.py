import os

filePath = input('Please Provide a file path - ')
if(os.path.exists(filePath)):
    os.remove(filePath)
    print('The file has been removed successfully')
else:    
    print('File Not Found')  
    filePath2 = input('Please Provide a correct file path - ')  
    if(os.path.exists(filePath2)):
        os.remove(filePath2)
        print('The file has been removed successfully')
    else:
        print('Try Again Later')
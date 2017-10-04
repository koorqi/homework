def is_palindrome(s):
    s=str(s)    # значение в строку
    s=s.replace(' ', '')   #убираем пробелы
    if s==s[::-1]:  # туда и обратно
        return True
    else:
        return False 

    
#print (is_palindrome('сел в озере березов лес'))


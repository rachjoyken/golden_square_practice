def factorial(n):
    product = 1
    while n > 0:
        n -= 1
        product *= n
    return product

print("Hello World!")
print (factorial(5))    

#terminal - pipenv --venv, copy and paste the path, click into '3.11.2' below, choose interactive path and paste. Then, press run and debug...you can choose break points by hovering over the 'gutter' and then 'step over' each line of code to see what's happening -> in this case, lines 4 and 5 should be swapped around.
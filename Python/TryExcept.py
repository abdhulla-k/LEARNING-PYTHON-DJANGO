#  The Try Except does privents the error
# Eg:
def Try():
    try:
       x = int(input('Enter and intiger: '))
       print(x)
    except ValueError:
        print('Your input is not a string value.')
        Try()
    else:
        print('all well')
    finally:
        print('all finished') 

Try()
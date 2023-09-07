def main():
    def check_palindrome(str_):
        cleanstr_=''.join(str_.split()).lower()
        #as mostly first letter of sentence is capital we need to make it lowercase
        if cleanstr_==cleanstr_[::-1]:

            return 1
    
        else:

            return 0

    #take user input
    sentence= input('Enter string: ')

    
    if check_palindrome(sentence):

        print(f'{sentence} is Palindrome')
    
    else:
        
        print(f'{sentence} is not Palindrome')


if __name__=='__main__':
     main()
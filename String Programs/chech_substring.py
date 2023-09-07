def check_substring(u_str,g_str):

    left=0

    for right in range(len(g_str)):
        
        if u_str[left] == g_str[right]:
            left=left+1

            if len(u_str) == left:
                break
        
        else:
            left=0

    if len(u_str) == left:
            return 1

    else:
        return 0



def main():

    given_str='Now is better than never.'
    user_input=input("Enter string:" )

    if check_substring(user_input,given_str):
        print(f'{user_input} exist in given_str')

    else:
        print(f'{user_input} does not exist in given_str')

     
if __name__=='__main__':
    main()
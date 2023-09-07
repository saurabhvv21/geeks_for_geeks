def reverse_str(g_str):
    
    return ' '.join(g_str.split()[::-1])

def main():
    
    given_str='The greatest glory in living lies not in never falling, but in rising every time we fall'
    
    print(f'given string  : {given_str} \nreverse string: {reverse_str(given_str)}')


if __name__=='__main__':
    main()    
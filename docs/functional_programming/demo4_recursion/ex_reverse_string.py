def reverse(string):
    if len(string) < 2:
        return string
    return reverse(string[1:]) + string[0]
    
r = reverse('1234')

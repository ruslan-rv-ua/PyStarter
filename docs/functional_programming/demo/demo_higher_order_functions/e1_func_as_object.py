def original_function():
    print('I am very cool function.')
    
# original_function

original_function()
function_ref = original_function
del original_function
function_ref()
original_function()

function_ref.__name__

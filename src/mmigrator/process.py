import functools
import sys


def process(cmd):
    def outer_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            sys.stdout.write(f'\r{cmd}...')
            
            func(*args, **kwargs)
            
            sys.stdout.flush()
            sys.stdout.write(f'\r{cmd}...Done\n')
        
        return wrapper
    
    return outer_wrapper

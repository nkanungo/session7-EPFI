import pytest
import session7
import os
#import numpy as np
import inspect
import re

README_CONTENT_CHECK_FOR = [
     
]

CHECK_FOR_THINGS_NOT_ALLOWED = [
    
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 400, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 6

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session7)
    spaces = re.findall('\n +.', lines)
    line_no =1
    for space in spaces:
        line_no +=1
        print('=====', line_no, space)
        #print(lines)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        #assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 
        assert re.search('[a-zA-Z#@=1234\'\"]', space), "Your code intentation does not follow PEP8 guidelines"
        assert len(re.sub(r'[a-zA-Z#@=1234\n\"\']', '', space)) % 4 == 0, \
        "Your code intentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_not_number_valueerror():
    with pytest.raises(ValueError):
        session7.check_fibonocci('a')


def test_fib_func():
    assert session7.check_fibonocci(5) == True , "Your Fibonocci function is not working" 
    assert session7.check_fibonocci(7) == False , "Your Fibonocci function is not working" 

def test_two_iter_func():
    assert session7.f([1,22,33,4],(1,3,2,7)) == [25, 11] , "Your function is not working" 
def test_strip_vowel_func():
    assert session7.strip_vowels("tsai") == 'ts' , "Your strip vowel function is not working" 
def test_relu_func():
    assert session7.relu_func([1,2,3,4,0,-1,-2]) == [1, 2, 3, 4, 0, 0, 0] , "Your relu function is not working" 
def test_sigmoid_func():
    assert session7.sigmoid_func([12,1]) == [0.9999938558253978, 0.7310585786300049] , "Your sigmoid function is not working" 
def test_shift_char_func():
    assert session7.shift_alphabets('tsai') == 'yxfn' , "Your shift character function is not working" 
    assert session7.shift_alphabets('txvu') == 'ycaz' , "Your shift character function is not working"

def test_profanity_func():
    passage= 'the lazy fox ran behind the pussy cat and wealth dog in the room for a while nihar prasanna android apple macintosh'
    assert session7.profanity_check(passage) == ['lazy','fox','behind','wealth','room','while','nihar','prasanna','android','macintosh'] , "Your profanity filter function is not working" 

def test_add_even_no_func():
    l1=[2,3,5,6,8,11,12,15,22]
    assert session7. add_even_no(l1) == 50 , "Your add even number function is not working"   

def test_big_char_func():
    l1='iAMthegoodZz'
    assert session7.find_biggest_char(l1) == 'z' , "Your big character function is not working"     
    
def test_add_every_3rd_func():
    l1=[2,3,5,6,8,11,12,15,22]
    assert session7.add_every_third_no(l1) == 38 , "Your shift character function is not working" 

def test_generate_number_plate_func():
    assert len(session7.generate_number_plate()) == 15 , "Your big character function is not working" 

def test_generate_number_plate_change_state_code_func():
    state_code = 'OD'
    assert session7.get_number_plate(state_code)[0][0:2] == 'OD' , "Your big character function is not working"      
    state_code = 'DL'
    assert session7.get_number_plate(state_code)[0][0:2] == 'DL' , "Your big character function is not working"      
    assert len(session7.get_number_plate(state_code)[0]) == 10 , "Your big character function is not working"      
 
def test_things_not_allowed():
    code_lines = inspect.getsource(session7)
    for word in CHECK_FOR_THINGS_NOT_ALLOWED:
        assert word not in code_lines, 'Have you heard of Pinocchio?'

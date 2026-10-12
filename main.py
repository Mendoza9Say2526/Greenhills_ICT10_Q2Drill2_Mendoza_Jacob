# Candidate Verification System
from pyscript import display, document


def name_finder (e):
    document.getElementById('result').innerHTML = ' ' # clear the divs
    first_name = document.getElementById('firstname').value.title().strip() # collecting input 1
    last_name = document.getElementById('lastname').value.title().strip() # collecting input 2
    full_name = first_name + ' ' + last_name # concatenating
    sapphire_students = ['Franco Deocampo', 'Alexa Agnote', 'Princess Sagum', 'Marcus Viray', 'Jaena Ambata', 'Leane Gabia', 'Katharine Peñas'] #list of students in ICT club
    student_checker = full_name in sapphire_students # member checker

    display_message = (f'Sorry {full_name}, we cannot find your name in the list', f'Congratulations {full_name}, you are now part of the ICT club!') # message output
    display(display_message[student_checker], target = 'result') # displaying the message
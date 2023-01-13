"""
stages were taken from tutorial at 
https://inventwithpython.com/invent4thed/chapter8.html 
"""
STAGES = [   
   # final state: head, torso, both arms, and both legs
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    # head, torso, both arms, and one leg
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
    # head, torso, and both arms
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
    # head, torso, and one arm
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
    # head and torso
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
    # head
    """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
    # initial empty state
    """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
]

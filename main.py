# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scoring_player1 = 'Ruud Gullit'
scoring_player2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scoring_player1 + ' ' + str(goal_0) + ', ' + scoring_player2 + ' ' + str(goal_1)

report = (f'{scoring_player1} scored in the {goal_0}nd minute\n{scoring_player2} scored in the {goal_1}th minute')

player = 'John Bosman'
first_name = player[:player.find(' ')]
last_name_len = len(player[player.find(' ')+1:])
name_short = 'J. Bosman'

#chant = f"{first_name}!\n" * len(first_name)
chant = 'John! John! John! John!'
good_chant = chant[-1] != ' '

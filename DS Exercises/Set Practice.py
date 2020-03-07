football = set(['John', 'Jack', 'Jason', 'Justin', 'Ivan', 'Ryan', 'Paul', 'Simon', 'Leon', 'Noah'])
soccerball = set(['Noah', 'Mark', 'Michael', 'Ivan', 'Gal', 'Daniel', 'Ben', 'Ryan'])
basketball = set(['Lucas', 'Noah', 'Andrew', 'Jason', 'Leon', 'Paul', 'David'])

print('Students in any of the three sports:', ', '.join(football|soccerball|basketball))
print('Students who play both soccer and basketball:', ', '.join(soccerball&basketball))
print('Students who play one sport only:', ', '.join(football^soccerball^basketball))
print('Students who play all three sports:', ', '.join(football&soccerball&basketball))
print('Students who play soccer and football, but not basketball:', ', '.join((soccerball&football)-basketball))

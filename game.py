player = {
  'name': 'Manuel',
  'attack': 10,
  'heal': 16,
  'health': 100
}
monster = {
  'name': 'Max',
  'attack': 12,
  'health': 100
}
game_running = True

while game_running == True:

  player_won = False
  monster_won = False
  print("Please select action")
  print("1) Attack")
  print("2) Heal")

  player_choice = input()

  if int(player_choice) == 1:
    monster['health'] -= player['attack']
    if monster['health'] <= 0:
      player_won = True
    else:
      player['health'] -= monster['attack']
      if player['health'] <= 0:
        monster_won = True
    print(player['health'])
    print(monster['health'])


  elif int(player_choice) == 2:
    print("Heal player")
  else:
    print("Enter valid input")

  if player_won == True or monster_won == True:
    game_running = False

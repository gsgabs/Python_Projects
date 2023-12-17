
def winner(player, bot):
  if player == bot:
    return "Empate"
  if player == 0 and bot == 1:
    return "Computer wins..."
  if player == 0 and bot == 2:
    return "Player wins!"
  if player == 1 and bot == 0:
    return "Player wins!"
  if player == 1 and bot == 2:
    return "Computer wins..."
  if player == 2 and bot == 0:
    return "Computer wins..."
  if player == 2 and bot == 1:
    return "Player wins!"
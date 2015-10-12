import learntocode
import learntocode.lessons.dance as dance
from learntocode.lessons.dance import *

learntocode.config.USER_ID = "Bananarama"

dance.add_dance_move("Test", "Do the test")
for key, value in dance.list_available_moves().items():
  print(key, value)

print(add_dance_routine("Test2", ["Test", "Test", "Test"]))
print(get_dance_routine("Test2"))
print(add_move_to_routine("Test2", "Test"))
print(get_dance_routine("Test2"))

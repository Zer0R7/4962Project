from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import TwitterSenseHat
import EmailSenseHat

sense = SenseHat()
sense.show_message("Home")

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        TwitterSenseHat.main()

    
def pushed_left(event):
    if event.action != ACTION_RELEASED:
        EmailSenseHat.main()

sense.stick.direction_right = pushed_right
sense.stick.direction_left = pushed_left
pause()

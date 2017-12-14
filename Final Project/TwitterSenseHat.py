def main():
    from twython import TwythonStreamer
    from sense_hat import SenseHat
    from auth import (
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
                    
    sense = SenseHat()
    sense.load_image("twitterbird.png")

    def pushed_middle(event):
            sense.clear
            import MasterFile

    sense.stick.direction_middle = pushed_middle
    
    class MyStreamer(TwythonStreamer):
        def on_success(self,data):
            if 'text' in data:
                username = data['user']['screen_name']
                tweet = data['text']
                sense.show_message("@{}: {}".format(username, tweet))
                
    stream = MyStreamer(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
            
    stream.statuses.filter(track='raspberrypiorc')
   

# My-Discord-Bot
Discord bot for my server using Discord.py

The bot has 3 iterations so far.  
The first one was a test run to see if I can get the bot up and running at least.  
The second one has a few commands that it can run for the user.  
The third one is a full soundboard that I can edit for use later, playing videos based on a defined library (or videos straight from youtube or other sources).  


First Bot:  
Says hello back to whoever types "!hello" in the chat while the bot is active.  

Second Bot:  
?eight_ball = Responds to a question like a magic eight ball  
?coin_flip = Flips a coin (returns heads or tails)  
?square X = squares the number X  

Third Bot:  
%join X = Bot joins X voice channel  
%summon = Bot joins voice channel of user who typed the message  
%play X = Bot plays X sound from dictionary if present, and otherwise plays audio from X video from youtube  
%volume X = Bot sets audio volume to X  
%pause = Pauses audio  
%resume = Resumes audio  
%stop = Leaves voice channel altogether  
%skip = Skips current video and goes to the next  
  
# Requirements
pip install discord.py  
pip install python-dotenv
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/TG-V4MP1R3/Alexa-Bot.git
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Alexa-Bot
fi
cd /Alexa-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot.... made by V4MP1R3"
python3 bot.py

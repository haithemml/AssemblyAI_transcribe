# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use pip3 instead of pip.

import assemblyai as aai

# Replace with your API key
aai.settings.api_key = "*************************************"

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

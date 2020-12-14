#Remove this line before deploying
_____REMOVE_THIS_LINE_____=True

# ENTER BOT TOKEN (Get your BOT_TOKEN by talking to @botfather)
BOT_TOKEN = "1492782745:AAGrsy77-jvuYEUaPdTDuzTCLF25QybL98w"
GDRIVE_FOLDER_ID = "1Wg0cOqiFtPTwkH8IhrFfsdMFLviiEu3y"
OWNER_ID = 1369147060
DOWNLOAD_DIR = "/home/username/mirror-bot/downloads"
DOWNLOAD_STATUS_UPDATE_INTERVAL = 5
AUTO_DELETE_MESSAGE_DURATION = 20
IS_TEAM_DRIVE = "True"
INDEX_URL = "https://myindexfile.djalam300.workers.dev"
USER_SESSION_STRING = "BQDDHjsFNoyKDfkgyV63qVTao888x8Jo8h9ggvSJyvB7BW9q0jLP7AQzayG42bNmEJYVBqaUheb7qh4kVTpsHxxF6HDWr2khlSqldH113RAslndHBfnKnFn_xHUg5laOVRujgYdsDqde97QAuJMY59Oftr4Y2XU1jdyvX69nBt_TsrvHFq5DJn3_PbNcMl1BtqXn5kFDb78CHGIyCorlLoj-Khg-rolOYGom4Hp4bBFzcOIHoJBjvEzDr2ovb7ffbzEAcqozJx5CbjCPxXDrfDn0mB8gyh4IDotz4lcsmytjpgONgnUPmN4JVUBhX3VagLnTaWvL6uXs9QsOIDBfby0eUZuGtAA"
TELEGRAM_API = 2782858
TELEGRAM_HASH = "7abf4b63274efe3e60d627a9b50a43bd"
USE_SERVICE_ACCOUNTS = ""

# --------------------------------------

# dont edit below this >



BOT_TOKEN = os.environ.get('BOT_TOKEN', BOT_TOKEN)
GDRIVE_FOLDER_ID = os.environ.get('GDRIVE_FOLDER_ID', GDRIVE_FOLDER_ID)
OWNER_ID = int(os.environ.get('OWNER_ID', OWNER_ID))
AUTHORISED_USERS = json.loads(os.environ.get('AUTHORISED_USERS', json.dumps(AUTHORISED_USERS)))
INDEX_URL = os.environ.get('INDEX_URL', INDEX_URL)
IS_TEAM_DRIVE = stb(os.environ.get('IS_TEAM_DRIVE', str(IS_TEAM_DRIVE)))
USE_SERVICE_ACCOUNTS = stb(os.environ.get('USE_SERVICE_ACCOUNTS', str(USE_SERVICE_ACCOUNTS)))

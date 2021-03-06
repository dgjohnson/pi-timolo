# User Configuration variable settings for pitimolo
# Purpose - Motion Detection Security Cam
# Updated - 4-May--2017 Must have pi-timolo.py ver 5.00 or greater
# Done by - Claude Pageau

configTitle = "pi-timolo Default Settings"
configName  = "config.py"

#======================================
#       pi-timolo.py Settings
#======================================

# Logging and Debug Settings
# Note - Set to False if script is run in background or /etc/rc.local
# --------------------------
verbose = True             # default= True Sends logging Info to Console. False if running script as daeman
logDataToFile = False      # default= False True logs diagnostic data to a disk file for review
debug = False              # default= False True = debug mode returns pixel average data for tuning
imageTestPrint = False     # default= False Set to True to print one image and exit (useful for aligning camera)

# Image Settings
# --------------
imageNamePrefix = 'cam1-'  # default= 'cam1-' for all image file names. Eg garage-
imageWidth = 1024          # default= 1024 Full Size Image Width in px  
imageHeight = 768          # default= 768  Full Size Image Height in px 
imageVFlip = False         # default= False True Flips image Vertically
imageHFlip = False         # default= False True Flips image Horizontally
imageRotation = 0          # Default= 0  Rotate image. Valid values: 0, 90, 180, 270
noNightShots = False       # default= False True=No Night Images (Motion or Timelapse)
noDayShots = False         # default= False True=No Day Images (Motion or Timelapse)
imagePreview = False       # default= False True=Preview image on connected RPI Monitor
useVideoPort = False       # default= False True=Use the video port to capture motion images (faster than the image port).

# Low Light Twilight and Night Settings
# -------------------------------------
nightTwilightThreshold = 80 # default= 80 dayPixAve where twilight starts (framerate_range shutter)
nightDarkThreshold = 50     # default= 50 dayPixAve where camera variable shutter long exposure starts
nightBlackThreshold = 4     # default= 4 dayPixAve where almost no light so max settings used
nightSleepSec = 30          # default= 30 Sec - Time period to allow camera to calculate low light AWB
nightMaxShutSec = 6.0       # default= 6.0 Sec Highest V1 Cam shutter for long exposures V2=10 Sec.
nightMaxISO  = 800          # default= 800 Night ISO setting for Long Exposure below nightThreshold
nightDarkAdjust = 0.4       # default= 0.4 Factor to fine tune nightDarkThreshold brightness (greater is brighter)

# Date/Time Settings for Displaying info Directly on Images
# ---------------------------------------------------------
showDateOnImage = True     # default= True False=Do Not display date/time text on images
showTextFontSize = 18      # default= 18 Size of image Font in pixel height
showTextBottom = True      # Location of image Text True=Bottom False=Top
showTextWhite = True       # Colour of image Text True=White False=Black
showTextWhiteNight = True  # default=True Changes night text to white.  Useful if night needs white text instead of black

# Motion Detect Settings
# ----------------------
motionOn = True            # default= True True=Turns Motion Detect On, False=Off
motionPrefix = "mo-"       # default= "mo-" Prefix for all Motion Detect images
motionDir = "media/motion" # default= "media/motion"  Folder Path for Motion Detect Image Storage
motionCamSleep = 0.7       # default= 0.7 Sec of day sleep so camera can measure AWB before taking photo
motionThreshold = 50       # default= 50 (1-200)  How much a pixel has to change to be counted
motionSensitivity = 100    # default= 100 Number of changed pixels to trigger motion image
motionAverage = 20         # default= 20 Num Images to Average for motion verification: 1=last image only, 100=Med, 300=High, Etc.
motionVideoOn = False      # default= False  True=Take a video clip rather than image
motionVideoTimer = 10      # default= 10 seconds of video clip to take if Motion Detected
motionQuickTLOn = False    # default= False  True=Take a quick time lapse sequence rather than a single image (overrides motionVideoOn)
motionQuickTLTimer = 10    # default= 10 Duration in seconds of quick time lapse sequence after initial motion detected
motionQuickTLInterval = 0  # default= 0 seconds between each Quick time lapse image. 0 is fast as possible
motionForce = 3600         # default= 3600 seconds (1 hr) Force single motion image if no Motion Detected in specified seconds.
motionNumOn = True         # default= True  True=filenames by sequenced Number  False=filenames by date/time
motionNumStart = 1000      # default= 1000 Start 0f motion number sequence
motionNumMax  = 500        # default= 0 Max number of motion images desired. 0=Continuous
motionNumRecycle = True    # default= True when NumMax reached restart at NumStart instead of exiting
motionStreamOn = False     # default= False  True=Use video stream thread for motion detect
motionStreamStopSec = 0.5  # default= 0.5 seconds  Time to close stream thread
motionDotsOn = True        # default= True Displays motion loop progress dots if verbose=True False=Non
motionDotsMax = 100        # default= 100 Number of motion dots before starting new line if motionDotsOn=True
createLockFile = False     # default= False True=Create pi-timolo.sync file whenever images saved. 
                           # Lock File is used to indicate motion images have been added
                           # so sync.sh can sync in background via sudo crontab -e

# Time Lapse Settings
# -------------------
timelapseOn = True         # default= False True=Turn timelapse On, False=Off
timelapsePrefix = "tl-"    # default= "tl-" Prefix for All timelapse images with this prefix
timelapseDir = "media/timelapse" # default= "media/timelapse"  Storage Folder Path for Time Lapse Image Storage
timelapseCamSleep = 4.0    # default= 4.0 seconds day sleep so camera can measure AWB before taking photo
timelapseTimer = 300       # default= 300 (5 min) Seconds between timelapse images
timelapseNumOn = True      # default= True filenames Sequenced by Number False=filenames by date/time
timelapseNumStart = 1000   # default= 1000 Start of timelapse number sequence
timelapseNumMax = 2000     # default= 2000 Max number of timelapse images desired. 0=Continuous
timelapseNumRecycle = True # default= True Restart Numbering at NumStart  False= Surpress Timelapse at NumMax
timelapseExitSec = 0       # default= 0 seconds Surpress Timelapse after specified Seconds  0=Continuous

#======================================
#       webserver.py Settings
#======================================

# Left iFrame Image Settings
# --------------------------
web_image_height = "768"       # default= "768" px height of images to display in iframe
web_iframe_width_usage = "75%" # Left Pane - Sets % of total screen width allowed for iframe. Rest for right list
web_iframe_width = "100%"      # Desired frame width to display images. can be eg percent "80%" or px "1280"
web_iframe_height = "100%"     # Desired frame height to display images. Scroll bars if image larger (percent or px)

# Right Side Files List
# ---------------------
web_max_list_entries = 0         # 0 = All or Specify Max right side file entries to show (must be > 1)
web_list_height = web_image_height  # Right List - side menu height in px (link selection)
web_list_by_datetime = True      # True=datetime False=filename
web_list_sort_descending = True  # reverse sort order (filename or datetime per web_list_by_datetime setting

# Web Server settings
# -------------------
web_server_root = "media"     # default= "media" webserver root path to webserver image/video folders
web_server_port = 8080        # default= 8080 Web server access port eg http://192.168.1.100:8080
web_page_title = "Pi-Timolo Media"  # web page title that browser show (not displayed on web page)
web_page_refresh_on = True    # False=Off (never)  Refresh True=On (per seconds below)
web_page_refresh_sec = "180"  # default= "180" seconds to wait for web page refresh  seconds (three minutes)
web_page_blank = False        # True Starts left image with a blank page until a right menu item is selected
                              # False displays second list[1] item since first may be in progress

# ---------------------------------------------- End of User Variables -----------------------------------------------------

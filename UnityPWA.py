import time,os,sys

def main():
    pageTitle = input("Project name:\n>>> ")
    os.system('cls')
    input("By pressing enter you agree to allow this tool to modify all the files in this folder to convert the build to a PWA. This may cause undesiered operation. The creator(s) of this program will not be held liable for damages. To cancel, push CTRL+C\n")
    os.system('cls')
    print("Creating PWA...\nDO NOT CLOSE THIS WINDOW\n\n")
    time.sleep(1)
    print("Purging old files...")
    time.sleep(0.5)
    print("Copying files...")
    time.sleep(0.7)
    print("Injecting PWA code...")
    time.sleep(0.5)
    print("Finalizing...")
    time.sleep(1)
    os.system('cls')
    print("Success! Please refer to the README.md file for further instructions.")
    time.sleep(0.7)
    print("\n\nTerminating in 5 seconds...")
    time.sleep(5)
    sys.exit()

def init():
    os.system('cls')
    print("Unity PWA Creator by Reuben Schiopu\nLoading...")
    time.sleep(2)
    print("Ready!")
    time.sleep(0.7)
    os.system('cls')
    main()

init()
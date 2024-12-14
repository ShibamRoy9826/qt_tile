from subprocess import DEVNULL, PIPE,  run
from os import getlogin, makedirs,  chdir, path, listdir,getcwd
from sys import stderr
from shutil import rmtree,move,copytree,copy

username=getlogin()

print("""
╔═══╗ ╔╗     ╔════╗  ╔╗     
║╔═╗║╔╝╚╗    ║╔╗╔╗║  ║║     
║║ ║║╚╗╔╝    ╚╝║║╚╝╔╗║║ ╔══╗
║║ ║║ ║║       ║║  ╠╣║║ ║╔╗║
║╚═╝║ ║╚╗     ╔╝╚╗ ║║║╚╗║║═╣
╚══╗║ ╚═╝     ╚══╝ ╚╝╚═╝╚══╝
   ╚╝                       
-------------------------------

Installation is is pretty simple, just answer a few questions in yes or no, and that's it! 
There's almost no bloat in the installer, you can deny to include anything that you don't want!
Incase you feel something is still bloat, raise an issue on the github repo.

When a question is asked, if you type 'exit' I abort the installation.
You can also just press enter to keep the default.
(Make sure to have an active internet connection before installation, and look for password prompts, I would often ask for passwords for muliple operations)
""")

def isinstalled(name):
    try:
        r=run(["pacman","-Qs",name],check=True,stdout=PIPE,stderr=DEVNULL)
        return bool(r.stdout.strip())
    except:
        return False

def isinextra(name):
    try:
        r=run(["pacman","-Ss",name],check=True,stdout=PIPE,stderr=DEVNULL)
        return bool(r.stdout.strip())
    except:
        return False


def installPackage(pkgName,url=""):
    if url=="":
        url=f"https://aur.archlinux.org/{pkgName}.git"
        if isinextra(pkgName):
            installPacman(pkgName)
        else:
            print(f"Installing: {pkgName}")
            try:
                print("- Cloning git repository...")
                if path.exists(pkgName):
                    rmtree(pkgName)

                    run(["git","clone",url],check=True)
                else:
                    run(["git","clone",url],check=True)
                chdir(pkgName)
                print("- Installing...")
                if not isinstalled(pkgName):
                    run(["makepkg","-si","--noconfirm"])
                print("Installed successfully!")

                chdir("..")
            except Exception as e:
                print(f"Error while installing {pkgName} , err:{e}",file=stderr)

    else:
        print(f"Installing: {pkgName}")
        try:
            print("- Cloning git repository...")
            run(["git","clone",url],check=True)
            chdir(pkgName)
            print("- Installing...")
            if not isinstalled(pkgName):
                run(["makepkg","-si","--noconfirm"])
            print("Installed successfully!")
            chdir("..")
        except Exception as e:
            print(f"Error while installing {pkgName} , err:{e}",file=stderr)



def installPacman(pkgName):
    print("#"*40,end="")
    print(f"| Installing and setting up {pkgName} |")
    print("#"*40)
    try:
        print("- Installing using pacman...")
        run(["sudo","pacman","-S","--noconfirm","--needed",pkgName])
        print("-"*40,end="")
        print(f"| Successfully installed {pkgName} ! |")
        print("-"*40)
    except:
        print(f"Error while installing {pkgName}",file=stderr)

def confApp(pkgName):
    print("#"*40,end="")
    print(f"| Configuring {pkgName} |")
    print("#"*40)
    try:
        pkgConf=f"/home/{username}/.config/{pkgName}"
        if path.exists(pkgConf):
            takeBackup(pkgConf)
        moveToConf(f"{getcwd()}/.config/{pkgName}",pkgName)

    except Exception as e:
        print(f"Error while configuring {pkgName},err: {e}",file=stderr)

def installPicom():
    print("#"*40,end="")
    print(f"| Installing and setting up Picom-pijulius |")
    print("#"*40)
    try:
        run(["git","clone","https://github.com/pijulius/picom.git"])
        chdir("picom")
        run("meson setup --buildtype=release build",shell=True)
        run("ninja -C build",shell=True)
        run("ninja -C build install",shell=True)
        chdir("..")
        confApp("picom")
        print("-"*40,end="")
        print(f"| Successfully installed picom ! |")
        print("-"*40)
    except Exception as e:
        print(f"Error while installing picom, err: {e}",file=stderr)
    
def takeBackup(p):
    # run(["mv",p,"~/.config/backup/"])
    try:
        move(path.expanduser(p),path.expanduser("~/.config/backup"))
    except:
        print("Files dont exist, no backups taken...")

def moveToConf(folder,confFolder):
    copytree(folder,path.expanduser(f"~/.config/{confFolder}/"))

def ask(msg):
    a=input(msg+ " (y/n): ")
    if a.lower()=="y" or a.lower()=="":
        print(f"Selected Yes.")
        return True
    elif a.lower()=="exit":
        print(f"Alright, aborting installation!")
        exit()
    elif a.lower()=="n":
        print(f"Selected No.")
        return False
    else:
        return ask("Please enter a valid input")

def askFloat(msg,default=None):
    a=input(msg+":")
    if a=="":
        return default
    try:
        res=float(a)
    except:
        return askFloat("Please enter a valid input (in decimals):")
    return res

def setupFont():
    print("#"*40,end="")
    print("| Installing and setting up Font |")
    print("#"*40)
    installPacman("unzip")
    try:
        makedirs("Iosevka")
    except:
        print("Folder exists.. Removing folder contents.. just in case...")
        rmtree("Iosevka")
        makedirs("Iosevka")
    chdir("Iosevka")
    run(['wget','https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/Iosevka.zip'])
    run(["unzip","Iosevka.zip"])
    chdir("..")
    run(["sudo","mv",getcwd()+"/Iosevka/","/usr/share/fonts/"],check=True)
    run(["fc-cache","-v"])
    print("-"*40,end="")
    print("| Finished font installation and setup |")
    print("-"*40)


def preInstall(mainpkgs,depends,mainpkgsAur,dependsAur):
    global username
    try:
        makedirs("temp")
        makedirs(f"/home/{username}/.config/backup")
    except:
        rmtree("temp")
        makedirs("temp")
    chdir("temp")

    depends.remove("Iosevka Nerd Fonts")
    depends.remove("unzip")
    if "+ Some asset files to be stored at ~/.local/share/qt_tile/" in depends:
        depends.remove("+ Some asset files to be stored at ~/.local/share/qt_tile/")


    if "colloid-catppuccin-gtk-theme-git" in mainpkgsAur:
        mainpkgsAur.remove("colloid-catppuccin-gtk-theme-git")
        mainpkgsAur.append("colloid-gtk-theme-git")

    # Installing all packages

    for i in depends:
        installPacman(i)


    setupFont()

    if "picom-pijulius" in mainpkgs:
        mainpkgs.remove("picom-pijulius")
        installPicom()

    for i in mainpkgs:
        installPacman(i)
    for j in dependsAur:
        installPackage(j)
    for j in mainpkgsAur:
        installPackage(j)


def setupUdev():
    run(["sudo","cp",".config/90-backlight.rules","/etc/udev/rules.d/"])

def postInstall():
    print("*"*40)
    print("Installation completed!!!! Please reboot to see full effects")

def runInstall(toSetup):
    try:
        rmtree("temp")
    except:
        pass
    
    confApp("qtile")
    print("Successfully setup qtile!")
    run(["sudo","usermod","-a","-G","video",username])

    if "kitty" in toSetup:
        confApp("kitty")
        print("Successfully setup kitty!")
    if "picom" in toSetup:
        takeBackup("~/.config/picom.conf")
        copy(getcwd()+"/.config/picom.conf",path.expanduser("~/.config/picom.conf"))
        print("Successfully setup picom!")

    if "libinput-gestures" in toSetup:
        takeBackup("~/.config/libinput-gestures.conf")
        copy(getcwd()+"/.config/libinput-gestures.conf",path.expanduser("~/.config/libinput-gestures.conf"))
        print("Successfully setup gestures!")
    if "zsh" in toSetup:
        run("chsh $(which zsh)",shell=True)
        takeBackup("~/.zshrc")
        copy(getcwd()+"/.config/.zshrc",path.expanduser("~/.zshrc"))
        print("Successfully setup zsh and zinit!")
    if "easyfeh" in toSetup:
        print("Successfully setup easyfeh!")
    if "rofi" in toSetup:
        confApp("rofi")
        print("Successfully setup rofi!")
    if "ncmpcpp" in toSetup:
        confApp("ncmpcpp")
        print("Successfully setup ncmpcpp!")

    if "mpd" in toSetup:
        confApp("mpd")
        print("Successfully setup mpd!")
        try:
            makedirs("/home/{username}/Music/MySongs")
        except:
            pass
    if "dunst" in toSetup:
        confApp("dunst")
        print("Successfully setup dunst!")
    if "scripts" in toSetup:
        copytree(getcwd()+"/.config/scripts",path.expanduser("~/scripts"))
    if "colloid-gtk-theme-git":
        takeBackup(path.expanduser("~/.config/gtk-3.0"))
        copytree(getcwd()+"/.config/gtk-3.0",path.expanduser("~/.config/gtk-3.0"))

    setupUdev()


dependencies=["qtile","wget","git","brightnessctl","Iosevka Nerd Fonts","papirus-icon-theme","zoxide","xdotool","unzip","python-psutil","python-mpd2"]
dependenciesAur=["qtile-extras-git","python-pulsectl","python-pulsectl-asyncio"]
toBeInstalled=[]
toBeInstalledAur=[]
moreToSetup=[]
toSetup=[]

script_list = """
- A water reminder notification script
- Automatic nightlight script 
- A script to fetch music mp3's from youtube (requires yt-dlp) to be played using mpd
- A script to show notification on plugging charger
- A script to show notification when any device is connected/disconnected
- Battery percentage alert scripts
"""

##$$$$$$ Terminal
term=ask("Do you want to install and configure kitty(terminal emulator) automatically?")
if term==False:
    termname=input("Alright! What do you want to use as your terminal emulator then? (Type exact name please, I will look into the AUR): ")
else:
    termname="kitty"

##########################################################

shell=ask("Do you want to install zsh (Comes with zinit)?")
if shell:
    p10k=ask("Do you want to setup powerlevel 10k as your zsh theme?")
else:
    p10k=False

easyfeh=ask("Do you want to install EasyFeh for color palette generation and wallpaper management?")
launcher=ask("Do you want to setup an app launcher(rofi)?")
powermenu=ask("Do you want to setup a powermenu(rofi)?")
extra_scripts=ask("Do you want to add extra scripts too? this list includes: \n"+script_list)
xclip=ask("Do you want to install xclip for clipboard management?")
dunst=ask("Do you want to setup a notification daemon? (dunst)")
cursors=ask("Do you want to install a different cursor theme? (catpuccin-cursors-mocha)")

##$$$$$ MPD
mpd=ask("Do you want to setup Music Player Daemon(MPD)?")
if mpd:
    ncmpcpp=ask("Do you want to setup ncmpcpp for mpd?")
else:
    ncmpcpp=False

############################################
recorder=ask("Do you want to install a screen recorder? (simplescreenrecorder)")
if recorder:
    recordername="simplescreenrecorder"
else:
    recordername=input("So, do you want to use some other screen recorder instead? (Empty for no recorder): ")

scrot=ask("Do you want to install scrot for taking screenshots?")
picom=ask("Do you want to install picom? it includes all the animations, blur, rounded corners and fancy stuff.. (pijulius fork)")
gestures=ask("Do you want to auto-setup touchpad gestures? (uses libinput-gestures)")

##$$$$$$ Browser
browser=ask("Do you want to install a browser?(zen-browser)")
if browser:
    browsername="zen-browser"
else:
    browsername=input("Okay.. So is there any other browser that you would like to install? (Type exact name please, I will look into AUR):")

############################################

flManager=ask("Do you want to install a file-manager?(thunar)")
##$$$$$$ File manager
if flManager:
    filemanager="thunar"
else:
    filemanager=input("Okay.. So is there any other file manager that you would like to install? (Type exact name please, I will look into the AUR):")


gtkTheme=ask("Do you want to install a GTK theme? (colloid-catppuccin-gtk-theme-git)")

##################################################################################################################
#### Adding all dependencies
if extra_scripts:
    dependenciesAur.append("yt-dlp")
    dependenciesAur.append("python-youtube-search-python")
    dependenciesAur.append("sct")
    dependencies.append("python-httpx")
    dependencies.append("+ Some asset files to be stored at ~/.local/share/qt_tile/")
    toSetup.append("scripts")

#### Adding all other packages

toBeInstalledAur.append(termname)
toSetup.append(termname)
toBeInstalledAur.append(browsername)
toBeInstalledAur.append(filemanager)

if recordername!="":
    toBeInstalledAur.append(recordername)
if shell:
    toBeInstalled.append("zsh")
    toBeInstalled.append("fzf")
    toBeInstalled.append("eza")
    moreToSetup.append("zinit")
    toSetup.append("zsh")
if easyfeh:
    toBeInstalledAur.append("easyfeh")
    toSetup.append("easyfeh")
if launcher or powermenu:
    toBeInstalled.append("rofi")
    toSetup.append("rofi")
if dunst:
    toBeInstalled.append("dunst")
    toSetup.append("dunst") 
if mpd:
    toBeInstalled.append("mpd")
    toBeInstalled.append("mpc")
    toSetup.append("mpd")
if ncmpcpp:
    toSetup.append("ncmpcpp")
    toBeInstalled.append("ncmpcpp")
if scrot:
    toBeInstalled.append("scrot")
if gestures:
    toBeInstalledAur.append("libinput-gestures")
if gtkTheme:
    toBeInstalledAur.append("colloid-catppuccin-gtk-theme-git")
    toSetup.append("colloid-catppuccin-gtk-theme-git")### TO WORK ON
if xclip:
    toBeInstalled.append("xclip")
if picom:
    toBeInstalled.append("picom-pijulius")
    dependencies.append("meson")
    dependencies.append("ninja")
    dependencies.append("uthash")
    toSetup.append("picom")


#### End of printing  questions
print("#"*40)
print("\n\nCool, all great, but there are a few things that are going to be installed as dependencies, not installing any of them can cause problems with other functions/features... Here's a list of them:")
for package in dependencies:
    print("  - ",package)

print("\nBesides, there's also a confirmation required, these are the things which are going to be installed except for the ones mentioned above:")
for package in toBeInstalled:
    print("  - ",package)
print("Oh, and I need to setup some stuff too:")
for package in moreToSetup:
    print(" - ",package)

confirm=ask("So... Are you alright with installation of all these packages?")

############### Starting/Aborting installation
if confirm:
    print("OkAy! StArTiNG tHe InStALlAtiOn rIgHt nOw!")
    preInstall(toBeInstalled,dependencies,toBeInstalledAur,dependenciesAur)
    runInstall(toSetup)
    postInstall()
else:
    print(f"Alright, aborting installation!")
    exit()

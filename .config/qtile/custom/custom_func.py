from subprocess import run

def runOnStartup(config):
    ## Removing animations from focus mode
    if config["mode_settings"]["mode"]=="focus":
        run("pkill picom",capture_output=False,shell=True)
    else:
        run("picom -b",capture_output=False,shell=True)

#!/usr/bin/python3

from os import getlogin

username=getlogin()
fl_path=f"/home/{username}/.config/easyfeh/full_palette.txt"
bg=""
fg=""
fg2=""
primary=""
secondary=""
urgent=""
with open(fl_path,"r") as f:
    a=f.readlines()
    for i in a:
        if i.startswith("bg"):
            bg=i.replace("bg:","").replace(";\n","")
        if i.startswith("primary"):
            primary=i.replace("primary:","").replace(";\n","")
        if i.startswith("secondary"):
            secondary=i.replace("secondary:","").replace(";\n","")
        if i.startswith("urgent"):
            urgent=i.replace("urgent:","").replace(";\n","")
        if i.startswith("fg2"):
            fg2=i.replace("fg2:","").replace(";\n","")
        elif i.startswith("fg"):
            fg=i.replace("fg:","").replace(";\n","")

content=f"""
* {{
    bg: {bg}99;
    bg2: {bg}55;
    fg: {fg};
    fg2: {fg2};
    primary: {primary};
    primary2: {primary}11;
    secondary: {secondary};
    secondary2: {secondary}11;
    urgent: {urgent};
}}
"""
rofi_colors="/home/shibam/.config/rofi/colors.rasi"
qtile_conf="/home/shibam/.config/qtile/config.toml"

with open(rofi_colors,"w") as fl:
    fl.write(content)

from toml import load,dump
with open(qtile_conf,"r") as f:
    c=load(f)

with open(qtile_conf,"w") as fl:
    c['colors']['bg']=f"{bg}80"[1:]
    c['colors']['bg2']=f"{bg}99"[1:]
    c['colors']['fg']=fg.replace(" ","")
    c['colors']['fg2']=fg2.replace(" ","")
    c['colors']['primary']=primary.replace(" ","")
    c['colors']['urgent']=urgent.replace(" ","")
    for ind,mode in enumerate(c["modes"]):
        c['modes'][ind]['normal_color']=bg[1:]
        c['modes'][ind]['focus_color']=fg2[1:]

    dump(c,fl)


try:
    import configparser
    p="/home/shibam/.config/cava/config"
    config = configparser.ConfigParser()
    config.read(p)
    config.set('color','foreground',f"'{fg}'".replace(" ",""))
    config.set('color','background','default'.replace(" ",""))
    config.set("color","gradient_color_1",f"'{secondary}'".replace(" ",""))
    config.set("color","gradient_color_2",f"'{primary}'".replace(" ",""))
    config.set("color","gradient_color_3",f"'{fg}'".replace(" ",""))
    config.set("color","gradient_color_4",f"'{fg2}'".replace(" ",""))


    with open(p,"w") as f:
        config.write(f)
except:
    pass

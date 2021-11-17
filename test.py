# Il faut un fichier qui servira à effectuer des conditions dessus
# Et un second fichier pour tout réécrire correctement

nfo_origin = open("file:///home/musubi42/Documents/Torrent/Created/1 Script/Bianca Gondolfo (FrontEndMasters) - JavaScript: From Fundamentals to Functional JS, v2 - Cours video(.wbpm) & exercice video (.webpm).txt", "r")
nfo_result = open("file:///home/musubi42/Documents/Torrent/Created/1 Script/Bianca Gondolfo (FrontEndMasters) - JavaScript: From Fundamentals to Functional JS, v2 - Cours video(.wbpm) & exercice video (.webpm).nfo", "w")

for line in nfo_origin:
    if line[0:7] == "Bite rate":
        nfo_result.write(line.replace("/run/media/musubi42/LaCie/Formation/Code With Mosh/", ""))
    else:
        nfo_result.write(line)
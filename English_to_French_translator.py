translation = {"house":"maison", "apple":"pomme", "tree":"arbre", "horse":"cheval", "yellow":"jaune", "keyboard":"clavier", "water":"eau", "start":"commencer", "city":"ville","ear":"oreille", "eel":"anguille", "tooth":"dent"}

def translate(key):
    if translation.has_key(key):
        print translation.get(key)
    else:
        print "Sorry that word doesn't exist in French!"

translate('horse')
# return 'cheval'
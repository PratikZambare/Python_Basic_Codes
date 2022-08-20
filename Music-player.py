from playsound import playsound
print("what is your mood today sir : sad / happy / exit")
playsound("mood.mp3")
i = input()
if i == "sad" or i == "Sad" :
    playsound("sadaudio.mp3")
    print("No probelm : ")
    playsound("playing.mp3")
    print("Playing.....")
    playsound("Bewafa.mp3")
elif i == "happy" or i == "Happy" :
    playsound("happyaudio.mp3")
    print("Select the song which you want to play")
    playsound("select.mp3")
    a = int(input("1. Akull / 2. Rataan : "))
    if a == 1 :
        print("Ohh Niceeee : ")
        playsound("playing.mp3")
        print("Playing Akull ... ")
        playsound("Akull.mp3")
    elif a == 2 :
        print("Ohh Niceeee : ")
        playsound("playing.mp3")
        print("Playing Rataan ... ")
        playsound("Rataan.mp3")
elif i == "exit" or i == "Exit":
    print("Chaala ja Bhosadike : ..")
    playsound("Chalajabhosdike.mp3")

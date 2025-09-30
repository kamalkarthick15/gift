import random
import time


print("""
╔══════════════════════════════════════╗
║    🎉🎉🎉 HAPPIEST BIRTHDAY 🎉🎉🎉║
║        🎂 SHARNI (Piroo playerrr) 🎂║
╚══════════════════════════════════════╝
""")


print("""
       🎂🎂🎂🎂🎂🎂🎂
      🎉🎉🎉🎉🎉🎉🎉🎉
    ✨✨✨✨✨✨✨✨✨✨
       🔥🔥🔥🔥🔥🔥
        🌟🌟🌟🌟🌟
         | | | | |
""")


messages = [
    "Hey, don't stress too much — life has a way of working itself out 💖",
    "Remember to smile even at small things; it makes the day brighter 😄",
    "Take your time, breathe, and don't let little annoyances get to you 🌸",
    "Believe in yourself — even the toughest bugs in life can be fixed 🚀",
    "Be kind to yourself and others; the world needs your light ✨",
    "Laugh often — it's the best way to debug a bad day 😆",
    "Trust the process; sometimes things take time to align ⏳",
    "Every day is a fresh start — make it your masterpiece 🎨"
]

fortunes = [
    "This year will bring you surprises and smiles 🎁",
    "Expect unexpected joys and happy moments ✨",
    "Adventure and laughter await you in the next 365 days 🚀",
    "Great achievements and happy memories are coming your way 🌟",
    "Your creativity and passion will lead to wonderful opportunities 💫"
]

print("✨ Wishing you joy, laughter, and endless good vibes 🌈\n")
print("💌 Special Messages for You:")
for i, msg in enumerate(random.sample(messages, k=random.randint(3, 4)), 1):
    print(f"   {i}. {msg}")

print(f"\n🔮 Birthday Fortune: {random.choice(fortunes)}\n")
print("From, your fellow Gamer team-mate 🎮\n")


print("Celebration time! 🎉🎊✨\n")
for _ in range(8):
    print("".join(random.choice("🎉✨💖🌟🎂🥳🎈🎊") for _ in range(35)))
    time.sleep(0.2)

print("\n🎂 HAPPY BIRTHDAY SHARNI! 🎂")
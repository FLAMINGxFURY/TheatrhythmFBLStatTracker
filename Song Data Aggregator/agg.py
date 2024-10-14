import pandas as pd

# import data
engine_data = pd.read_csv("Song Engine Data.csv")
trigger_data = pd.read_csv("Song Trigger Data.csv")

# Remove rows from engine data where eng_name is null
engine_data = engine_data[engine_data["eng_name"].notnull()]

# Change series in trigger data: 
#   "Final Fantasy" -> "Final Fantasy I"
#   "FF Mystic Quest" -> "Mystic Quest"
#   "FF Tactics" -> "Final Fantasy Tactics"
#   "FF Type-0" -> "Final Fantasy Type-0"
#   "Dissidia" -> "Dissidia Final Fantasy"
#   "Mobius FF" -> "Mobius Final Fantasy"
#   "Crystal Chronicles" -> "Crystal Chronicles Series"
#   "FF7:Remake" -> "Final Fantasy VII Remake"
#   "FF Series" -> "Final Fantasy Series"
#   "Chrono" -> "Square Enix Titles"
#   "Bravely Default" -> "Square Enix Titles"
#   "LIVE A LIVE" -> "Square Enix Titles"
#   "Mana" -> "Square Enix Titles"
#   "SaGa" -> "Square Enix Titles"
#   "NieR" -> "Square Enix Titles"
#   "Octopath Traveler" -> "Square Enix Titles"
trigger_data["series"] = trigger_data["series"].replace("Final Fantasy", "Final Fantasy I")
trigger_data["series"] = trigger_data["series"].replace("FF Mystic Quest", "Mystic Quest")
trigger_data["series"] = trigger_data["series"].replace("FF Tactics", "Final Fantasy Tactics")
trigger_data["series"] = trigger_data["series"].replace("FF Type-0", "Final Fantasy Type-0")
trigger_data["series"] = trigger_data["series"].replace("Dissidia", "Dissidia Final Fantasy")
trigger_data["series"] = trigger_data["series"].replace("Mobius FF", "Mobius Final Fantasy")
trigger_data["series"] = trigger_data["series"].replace("Crystal Chronicles", "Crystal Chronicles Series")
trigger_data["series"] = trigger_data["series"].replace("FF7:Remake", "Final Fantasy VII Remake")
trigger_data["series"] = trigger_data["series"].replace("FF Series", "Final Fantasy Series")
trigger_data["series"] = trigger_data["series"].replace("Chrono", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("Bravely Default", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("LIVE A LIVE", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("Mana", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("SaGa", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("NieR", "Square Enix Titles")
trigger_data["series"] = trigger_data["series"].replace("Octopath Traveler", "Square Enix Titles")

# Create a unique string for each song in engine data by combining eng_name, series, and ms_type
engine_data["full_name"] = engine_data["eng_name"] + engine_data["series"] + engine_data["ms_type"]

# Create a unique string for each song in trigger data by combining song_title, series, and ms_type
trigger_data["full_name"] = trigger_data["song_title"] + trigger_data["series"] + trigger_data["ms_type"]

# Set both fields to lowercase
engine_data["full_name"] = engine_data["full_name"].str.lower()
trigger_data["full_name"] = trigger_data["full_name"].str.lower()

# Add trig_basic, trig_expert, trig_ultimate, and trig_supreme to engine data where full_name matches
engine_data["trig_basic"] = engine_data["full_name"].map(trigger_data.set_index("full_name")["trig_basic"])
engine_data["trig_expert"] = engine_data["full_name"].map(trigger_data.set_index("full_name")["trig_expert"])
engine_data["trig_ultimate"] = engine_data["full_name"].map(trigger_data.set_index("full_name")["trig_ultimate"])
engine_data["trig_supreme"] = engine_data["full_name"].map(trigger_data.set_index("full_name")["trig_supreme"])

# save to csv
engine_data.to_csv("Combined Data.csv", index=False)

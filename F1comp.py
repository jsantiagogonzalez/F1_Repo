import fastf1 as ff1
from fastf1 import plotting
from fastf1 import api
from matplotlib import pyplot as plt

plotting.setup_mpl()

cache_dir = r"C:\Users\jsant\Documents\F1\CACHE"

ff1.api.Cache.enable_cache(cache_dir, ignore_version=False, force_renew=False, use_requests_cache=True)

race = ff1.get_session(2021, 'BRA', 'SQ')
laps = race.load_laps()

ver = laps.pick_driver('VER')
ham = laps.pick_driver('HAM')


fig, ax = plt.subplots()
ax.plot(ver['LapNumber'], ver['LapTime'], color='blue')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title("VER vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()
# downeaster-tracker
A ESP-32 based train tracker for the Amtrak Downeaster
# Inspiration
This project was inspired by the [TrainTrackr line of PCB based LED live train maps](https://www.traintrackr.io/). The PCB design is a mishmash of [their open source board design](https://github.com/Traintrackr/board_files) as well as various [ESP-32 PCB design youtube videos](https://www.youtube.com/watch?v=jiJGbWOSdMo) and online resources. 

# A footnote on the HT16K33
I have a mixed review of this LED driver. On one hand, its age and extensive use in the DIY electronics space means it has pretty robust support. On the other hand, it's old. I wasn't able to source any from the usual suspects (digikey, mouser, etc.) and resorted to picking some up on Ebay. The kicad footprint and symbol are in /PCB. Also, despite the datasheet saying otherwise, it seems as though it can run just fine at 3.3V, and is used extensively in production designs at that voltage.
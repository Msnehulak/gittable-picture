# Gitable Picture
Gitable Picture (GP) is a git extension for images. Main goal is to achieve origin+N image connection and low-cost image versioning. 

# How work in history 
In GP is original IMG in min repository. in history are stored only diffs. 

If I need oldest ver off img I need to add on ORG img all diffs

# How to create diff
1. Ad first we find diferencic between Original and different versions. 
2. Around change places create bound box
2.1 if one change is in top left and other on bottom right it is 2 boxis. 
3. After we have all boxes we take from org ing in area of boundi box and same pixels in org and verN swap to alfa 255 (invisible)
3.1 ve cen create visual diff by diff box switch if alfa > 0 = change. 
4. Output is saved with as lossless img format with X, y position where on org img it si. 

## notes
1. In code we use row binary files, diff is only save as png.

# Why choose us? 
1. We allow infinity version of img to be compressed to one. 
2. We can create GIF of how your img changed
3. We can create 3D representation of change history. 
4. We offer free websites wher you can tast 3-way mearge on your machine locally with Web assembly. 

# Progress 
Onli idea
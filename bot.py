#!/usr/bin/env python3
import sys, json

tick = 0
first_tick = True
animationtick = 0

for line in sys.stdin:
    if first_tick:
        with open("animation.json", "r") as f:
            frames_json = json.load(f)

        info = frames_json["meta"]
        x_size = info["x_size"]
        y_size = info["y_size"]
        frame_count = info["frame_count"]

    tick += 1
    highlights = []

    animationtick += 1
    if animationtick > frame_count:
        animationtick = 1

    frame_key = f"frame{animationtick}"
    frame_data = frames_json["frames"][frame_key]
    for i in range(5):
        for x in range(x_size):
            for y in range(y_size):
                highlights.append([
                    x,
                    y,
                    frame_data[f"row{y + 1}"][x]
                ])

    print("WATCH" ,json.dumps({"highlight": highlights}), flush=True)
    first_tick = False

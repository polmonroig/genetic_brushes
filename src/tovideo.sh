#!/bin/bash
ffmpeg -framerate 25 -i frames/sample_%04d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p frames/output.mp4

import sys
import subprocess
import os
from H_m3u8DL import m3u8download
import m3u8
master_url = 'https://vuclip-eip2.akamaized.net/007e58474e2960f50b0f79a16b16fad3/VP6_V20220607031940/P2/video/325a2962-2b80-470d-b9c7-fa4c475f8a10/vid_1080p_V20220610163600.m3u8'
m3u8download(master_url)
# m3u8boj = m3u8.load(master_url)
# print(m3u8boj.data)
#
# Copyright (C) 2021-2022 byMoni_Help@Github, < https://github.com/mukeshmoni >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Its_me_moni
# Rocks © @Its_me_moni
# Owner moni
# monish
# All rights reserved. © Alisha © Moni © Yukki


import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass

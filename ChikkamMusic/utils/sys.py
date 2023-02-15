#
# Copyright (C) 2021-2022 byMoni_Help@Github, < https://github.com/mukeshmoni >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @Its_me_moni
# Rocks © @Its_me_moni
# Owner moni
# monish
# All rights reserved. © Alisha © Moni © Yukki


import time

import psutil

from ChikkamMusic.misc import _boot_

from .formatters import get_readable_time


async def bot_sys_stats():
    bot_uptime = int(time.time() - _boot_)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    UP = f"{get_readable_time((bot_uptime))}"
    CPU = f"{cpu}%"
    RAM = f"{mem}%"
    DISK = f"{disk}%"
    return UP, CPU, RAM, DISK

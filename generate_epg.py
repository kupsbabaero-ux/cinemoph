#!/usr/bin/env python3
"""
CineMo! EPG Generator
Generates XMLTV EPG with current date/time (Philippines +0800)
Auto-updates for the next 7 days based on day of week.
Run this script anytime to refresh the EPG with current dates.
"""

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import os

PH_TZ = ZoneInfo("Asia/Manila")

# Block definitions (start_hour, end_hour, title, category)
# end_hour 25 means next day 01:00
WEEKDAY_BLOCKS = [
    (1, 5, "CineSilip", "Movie"),
    (5, 7, "Super Morning Sine", "Movie"),
    (7, 9, "CineTakilya", "Movie"),
    (9, 11, "CineKomedya", "Comedy"),
    (11, 13, "CineSaya", "Movie"),
    (13, 15, "CineAstig", "Action"),
    (15, 17, "CineKamao", "Action"),
    (17, 19, "CineTawanan", "Comedy"),
    (19, 21, "CineBarako", "Action"),
    (21, 23, "CineAksyon", "Action"),
    (23, 25, "CineKwela", "Movie"),
]

SATURDAY_BLOCKS = [
    (1, 4, "CineSilip", "Movie"),
    (4, 6, "Super Morning Sine", "Movie"),
    (6, 8, "CineDeKalibre", "Action"),
    (8, 10, "CineKilig", "Romance"),
    (10, 12, "CineSaya", "Movie"),
    (12, 14, "CineMatapang", "Action"),
    (14, 17, "FPJ's Batang Quiapo Marathon", "Action"),
    (17, 19, "CineMo! Box Office", "Movie"),
    (19, 21, "Dolphy: Hari ng Comedy", "Comedy"),
    (21, 23, "CineMaton", "Movie"),
    (23, 25, "CinePatok", "Movie"),
]

SUNDAY_BLOCKS = [
    (1, 5, "CineSilip", "Movie"),
    (5, 7, "Super Morning Sine / CineUna", "Movie"),
    (7, 9, "CineDeKalibre", "Action"),
    (9, 11, "CineKilig", "Romance"),
    (11, 13, "CineSaya", "Movie"),
    (13, 15, "Action / Feature Film", "Action"),
    (15, 17, "Weekend Movie Bonding", "Movie"),
    (17, 19, "CineMo! Box Office", "Movie"),
    (19, 21, "Markang Daboy / Special", "Movie"),
    (21, 23, "CineMaton", "Movie"),
    (23, 25, "CinePatok", "Movie"),
]


def format_xmltv_time(dt):
    """Format datetime to XMLTV: YYYYMMDDHHMMSS +ZZZZ"""
    return dt.strftime("%Y%m%d%H%M%S %z")


def generate_programme(start_dt, end_dt, title, category, channel="cinemo.ph"):
    return f'''  <programme start="{format_xmltv_time(start_dt)}" stop="{format_xmltv_time(end_dt)}" channel="{channel}">
    <title lang="en">{title}</title>
    <category lang="en">{category}</category>
  </programme>
'''


def make_aware(dt):
    """Ensure datetime is timezone-aware in PH time."""
    if dt.tzinfo is None:
        return dt.replace(tzinfo=PH_TZ)
    return dt.astimezone(PH_TZ)


def main():
    now = datetime.now(PH_TZ)
    # Start from today at 00:00 PH time
    start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)

    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">
<tv generator-info-name="CineMo EPG Generator" generator-info-url="https://github.com/yourusername/cinemo-epg">
  <channel id="cinemo.ph">
    <display-name lang="en">CineMo!</display-name>
    <display-name lang="tl">Cine Mo!</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/en/thumb/8/8e/Cine_Mo%21_logo.png/220px-Cine_Mo%21_logo.png"/>
  </channel>

'''

    for day_offset in range(7):  # Next 7 days
        day = start_date + timedelta(days=day_offset)
        weekday = day.weekday()  # 0=Mon ... 5=Sat, 6=Sun

        if weekday == 5:  # Saturday
            blocks = SATURDAY_BLOCKS
        elif weekday == 6:  # Sunday
            blocks = SUNDAY_BLOCKS
        else:
            blocks = WEEKDAY_BLOCKS

        for start_h, end_h, title, category in blocks:
            # Calculate start
            start_day = day
            start_hour = start_h
            if start_h >= 24:
                start_day = day + timedelta(days=1)
                start_hour = start_h - 24
            start_dt = make_aware(start_day.replace(hour=start_hour, minute=0, second=0, microsecond=0))

            # Calculate end
            end_day = day
            end_hour = end_h
            if end_h >= 24:
                end_day = day + timedelta(days=1)
                end_hour = end_h - 24
            end_dt = make_aware(end_day.replace(hour=end_hour, minute=0, second=0, microsecond=0))

            xml += generate_programme(start_dt, end_dt, title, category)

    xml += "</tv>\n"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, "cinemo.xml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"✅ Generated: {output_path}")
    print(f"📅 Generated at: {now.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"📺 Covers: {start_date.strftime('%Y-%m-%d')} → {(start_date + timedelta(days=6)).strftime('%Y-%m-%d')}")
    print("🔄 Re-run this script anytime to auto-update dates.")


if __name__ == "__main__":
    main()

# CineMo! EPG (XMLTV)

Electronic Program Guide for **CineMo!** (ABS-CBN Philippine movie channel) in standard XMLTV format.

## Files

| File | Description |
|------|-------------|
| `cinemo.xml` | Ready-to-use XMLTV EPG (7 days) |
| `generate_epg.py` | Python script that auto-updates dates based on current time |
| `.github/workflows/update-epg.yml` | GitHub Actions workflow – auto-updates EPG daily |

## Schedule Blocks

### Monday – Friday
- 01:00 – 05:00 → CineSilip
- 05:00 – 07:00 → Super Morning Sine
- 07:00 – 09:00 → CineTakilya
- 09:00 – 11:00 → CineKomedya
- 11:00 – 13:00 → CineSaya
- 13:00 – 15:00 → CineAstig
- 15:00 – 17:00 → CineKamao
- 17:00 – 19:00 → CineTawanan
- 19:00 – 21:00 → CineBarako
- 21:00 – 23:00 → CineAksyon
- 23:00 – 01:00 → CineKwela

### Saturday
- 01:00 – 04:00 → CineSilip
- 04:00 – 06:00 → Super Morning Sine
- 06:00 – 08:00 → CineDeKalibre
- 08:00 – 10:00 → CineKilig
- 10:00 – 12:00 → CineSaya
- 12:00 – 14:00 → CineMatapang
- 14:00 – 17:00 → FPJ's Batang Quiapo Marathon
- 17:00 – 19:00 → CineMo! Box Office
- 19:00 – 21:00 → Dolphy: Hari ng Comedy
- 21:00 – 23:00 → CineMaton
- 23:00 – 01:00 → CinePatok

### Sunday
- 01:00 – 05:00 → CineSilip
- 05:00 – 07:00 → Super Morning Sine / CineUna
- 07:00 – 09:00 → CineDeKalibre
- 09:00 – 11:00 → CineKilig
- 11:00 – 13:00 → CineSaya
- 13:00 – 15:00 → Action / Feature Film
- 15:00 – 17:00 → Weekend Movie Bonding
- 17:00 – 19:00 → CineMo! Box Office
- 19:00 – 21:00 → Markang Daboy / Special
- 21:00 – 23:00 → CineMaton
- 23:00 – 01:00 → CinePatok

## Auto-update

### Local
```bash
python3 generate_epg.py
```
This regenerates `cinemo.xml` with the current date + next 6 days using Philippine time (Asia/Manila, +0800).

### GitHub Actions (automatic)
The workflow `.github/workflows/update-epg.yml` runs **every day at 08:05 PH time** (00:05 UTC).

It will:
1. Run `generate_epg.py`
2. Commit & push the updated `cinemo.xml` if there are changes

You can also trigger it manually from the **Actions** tab → **Update CineMo EPG** → **Run workflow**.

## Usage

- Import `cinemo.xml` into any XMLTV-compatible EPG reader, PVR, or IPTV app (e.g. TiviMate, IPTV Smarters, Kodi, Jellyfin, etc.).
- Channel ID: `cinemo.ph`

## Notes

- Exact movie titles change daily. This EPG provides the **program blocks**.
- Times are in Philippine Standard Time (+0800).
- Generated for educational / personal use.

## License

Public domain / free to use and modify.

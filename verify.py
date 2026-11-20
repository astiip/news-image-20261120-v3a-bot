"""Verify news-image-20261120 v3a build.html: all 27 stories, 14 DATE CHECK items,
exact figures, region bar sum, number strip. Run from the repo dir."""
import html, re, sys

src = html.unescape(open("build.html").read())
# strip tags for text checks (keep visible text only)
text = re.sub(r"<[^>]+>", " ", src)
text = re.sub(r"\s+", " ", text)

stories = {
 1: ["400+ drones", "110+ missiles", "Podilsko-Voskresenskyi", "Darnytskyi", "Pivdennyi"],
 2: ["Gopalpur", "11:20am IST", "70–80", "gusting 90", "300,000+", "9,341 shelters"],
 3: ["COP31", "fossil-fuel mention", "500 Mt", "35%", "$120bn", "Panama"],
 4: ["GTA VI", "24.58m", "$2.36bn", "18.44m", "$1.77bn", "6.15m", "$588m", "11.21m", "$815.7m"],
 5: ["Nowy Lipowiec", "05:40 GMT", "Rudnik nad Sanem", "Mołodycz"],
 6: ["Rob Bonta", "Jensen Huang", "Nov 12", "02:18 UTC"],
 7: ["£5.1bn", "100,000 youth visas", "Burnham"],
 8: ["BepiColombo", "6bn miles", "9 flybys", "Saturday 21 Nov", "April 2027"],
 9: ["2.3%", "2.2%", "Dec 17–18", "1.5%", "3.00%", "3.50%", "18th month"],
 10: ["111", "smart glasses", "subminiature camera", "497,000"],
 11: ["56,436.65", "−5.06%", "4,869.96", "−5.21%", "36,033.29", "−6.23%", "22,410.80", "3,533.79", "SoftBank", "−14.5%"],
 12: ["CGIL", "€26bn", "$30bn", "Rome", "Milan", "Naples"],
 13: ["Daraxonrasib", "60.7%", "8.2%", "90.2%", "12.8 mo", "~77%"],
 14: ["KHARKIV", "4 hurt", "50+ windows"],
 15: ["XI HAILS AUSTRALIA", "Shenzhen"],
 16: ["RAONI, 94", "362,000 ha"],
 17: ["TWO TANKERS HIT MINES", "4m+ barrels", "Hormuz"],
 18: ["GEN Z REGELT", "73 cities"],
 19: ["BRAZIL SELLS $1BN", "5.93 reais"],
 20: ["IRAN WAR COST", "$48.3BN", "$47.1bn"],
 21: ["Kataib Hezbollah", "Jurf al-Sakhar"],
 22: ["ICJ RULING", "10,000 Rohingya"],
 23: ["SENATE BLOCKS IRAN VOTE", "48–51"],
 24: ["RIO TINTO PAYS $250M", "Panguna"],
 25: ["POLAND GAS PACT", "Hungary", "Czechia", "Slovakia", "Lithuania"],
 26: ["14-TANKER CONVOY", "Kharg Island", "$92.77"],
 27: ["25+ COUNTRIES"],
}
dc = ["Trump–Xi–Putin Shenzhen declaration", "ICJ: Myanmar guilty, 9–6",
      "Anthropic IPO $83→$97.17, $81.3bn", "GTA VI midnight launch (Metacritic 99)",
      "COP31 draft two drops fossil fuels", "Suneung: 550,000+ sit the exam",
      "Akvan nears Odisha", "130 pupils freed, Nigeria", "Australia jobs 4.9%",
      "Fiona the hippo dies, 9", "Tonga declares drought emergency",
      "Dakar boat capsize: 4 dead", "Indonesia asset-forfeiture law", "Bukele seeks third term"]

fails = []
for n, phrases in stories.items():
    for p in phrases:
        if p not in text:
            fails.append(f"story {n}: missing {p!r}")
for item in dc:
    if item not in text:
        fails.append(f"DATE CHECK: missing {item!r}")

# forbidden wrong numbers must NOT appear
for bad in ["gusting 110", "−6.63%"]:
    if bad in text:
        fails.append(f"FORBIDDEN present: {bad!r}")

# dropped v1 stories must NOT appear (27 only)
for bad in ["Russell 1:47.272", "Nicholls 175*", "UK RETAIL +0.7%", "NEPAL PM TO VISIT INDIA",
            "ATP TURIN", "TONGA SCHOOLS CLOSE EARLY", "85% OF RESCUE FLEET DOWN",
            "METHANE RULES DELAYED"]:
    if bad in text:
        fails.append(f"DROPPED story still present: {bad!r}")

# region bar sums to 27
m = re.findall(r"(EUROPE|ASIA|MIDDLE EAST|AMERICAS|OCEANIA|GLOBAL) (\d+)", text)
total = sum(int(v) for _, v in m)
if total != 27 or len(m) != 6:
    fails.append(f"region bar: {m} sums to {total}, want 6 regions = 27")
# number strip figures
for p in ["8 killed", "300,000+", "−6.23%", "$2.36bn", "111", "60.7%"]:
    if p not in text:
        fails.append(f"strip: missing {p!r}")

print(f"stories checked: {len(stories)}, date-check items: {len(dc)}, regions: {m} = {total}")
if fails:
    print("FAILURES:")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("ALL CHECKS PASSED")

// news-image-20261120 v3a — "The Friday Ledger: Front Page, 27 stories"
// Friday 20 November 2026, told as a classic centred front page: a giant
// serif date masthead, a six-number strip, a region bar, four big
// illustrated leads in a 2x2 grid (Kyiv / Akvan / COP31 / GTA VI), eight
// medium cards in a 4-column row, then a dotted world map beside a numbered
// index for the other 15 stories, and a DATE CHECK stamp strip for
// 19 November. Alternative variant of v2 ("Five Acts") at the user's order:
// the user found v2 lacking and asked for another poster option. Same 27
// verified stories as v2, all figures re-checked by verify.py; no UTC time
// bands and no right rail here — a deliberately different composition from
// v2 and from the leaderboard's entries. The entry image is produced by
// build.html and stored as entry.png; this program copies it to the output
// directory, byte for byte, so both runs write identical bytes.
// No network is used.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "out";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));

# Sessile

![sessile render](.images/render.webp)

*Sessile* is a further exploration of "minimal" finger travel.

## What Even Is 'Minimal Finger Travel' Anyway?

Probably the least amount of finger travel would be not moving them at all. That would be 10 keys...

```math
combos_{10\,keys} = \sum_{r=1}^{10} C(10, r) = 1023
```

...yielding 1023 possible combinations. 

More realistically, we might consider excluding cross hand combinations so that modifiers might be used. That would give us 

```math
combos_{5\,keys} = \sum_{r=1}^{5} C(5, r) = 31
```

So, with only 5 keys on both hands, and no cross hand combos, we would have a total of 62 possible keys per layer—more than sufficient.

I wasn't quite ready to take on learning to type on that though, so just avoiding lateral reaches seemed like a start. 🙃


## Features

- Sessile uses KLP-Lame keycaps. Larger caps may be tight, especially on the bottom row. I was lazy and didn't model the tilted keycaps in the rendering, but they're much nicer for the vertical combos.

- Uses battery LIR1254. DO NOT substitute LR44. 

- The high speed pins were left available for encoders and *could* be wired in a subsequent revision.

- Built with RMK. ~~Combos soon to follow upon upstream merge.~~ Combos are here! But only 8 of them at a time. Configure them in [Vial](https://get.vial.today).

## Production Files

You can find the gerbers, bom, and cpl for JLC [here](board/output/pcbs/jlcpcb/production_files/). Finished boards are available [here](https://octule.com/listing/1842172090/sessile)


## Origin

*Sessile* was produced using [studyofhands](https://github.com/willpuckett/studyofhands). 

![study of hands](.images/sessile_study.svg)

## Firmware

There are two firmwares for this board--zmk and rmk. Go with zmk if you want something smoother and fully featured. Use rmk if you're punk rock. 😏

Using a dongle will greatly increase battery life.

To use zmk without a dongle flash [sessile_central.uf2](out/sessile_central.uf2). To use zmk with a dongle, flash [sessile_peripheral.uf2](out/sessile_peripheral.uf2) to the board and [sessile_dongle.uf2](out/sessile_dongle.uf2) to a nice-nano-v2 (or supermini).

rmk can also be configured for dongle mode but currently only has pre-built firmware in [central mode](rmk/sessile.uf2).

The zmk build has a magic/arcane key. It takes some getting used to, but is allegedly far more efficient (about half the effort) according to the new version of [cyanophage](https://cyanophage.github.io/magic?layout=bfdlq-pouyjcstrzxnaihkvgmw%5C%2F.%2C%27%3B%3De&mode=ergo&lan=english) that now accounts for such things (alt-click to set a magic key).

Both zmk and rmk flashed boards can be configured via their guis... [Vial](https://get.vial.today) for rmk and [ZMK Studio](https://zmk.studio/download) for zmk.


## Keymap

![Caster Befuddle Variant](.images/keymap_caster.svg)



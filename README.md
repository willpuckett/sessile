# 🧽 Sessile

![sessile render](.images/render.webp)

[![Build RMK firmware](https://github.com/willpuckett/sessile/actions/workflows/rmk.yml/badge.svg)](https://github.com/willpuckett/sessile/actions/workflows/rmk.yml)
[![keymap](https://github.com/willpuckett/sessile/actions/workflows/keymap.yml/badge.svg)](https://github.com/willpuckett/sessile/actions/workflows/keymap.yml)

_Sessile_ is a further exploration of "minimal" finger travel.

## 🤔 What Even Is 'Minimal Finger Travel' Anyway?

Probably the least amount of finger travel would be not moving them at all. That
would be 10 keys...

```math
combos_{10\,keys} = \sum_{r=1}^{10} C(10, r) = 1023
```

...yielding **1023** possible combinations.

More realistically, we might consider excluding cross hand combinations so that
modifiers might be used. That would give us

```math
combos_{5\,keys} = \sum_{r=1}^{5} C(5, r) = 31
```

So, with only 5 keys on both hands, and no cross hand combos, we would have a
total of **62** possible keys per layer—more than sufficient.

I wasn't quite ready to take on learning to type on that though, so just
avoiding lateral reaches seemed like a start. 🙃

## ✨ Features

- 🧩 Sessile uses KLP-Lame keycaps. Larger caps may be tight, especially on the
  bottom row. I was lazy and didn't model the tilted keycaps in the rendering,
  but they're much nicer for the vertical combos.

- 🔋 Uses battery LIR1254. **DO NOT substitute LR44.**

- 🔌 The high speed pins were left available for encoders and _could_ be wired
  in a subsequent revision.

- ⚙️ Built for RMK. Configure using [Vial](https://get.vial.today).

## 📦 Production Files

You can find the gerbers, bom, and cpl for JLC
[here](board/output/pcbs/jlcpcb/production_files/). Finished boards are
~~available~~ [sold out](https://octule.com/listing/1842172090/sessile) till the
next batch.

## 🎨 Origin

_Sessile_ was produced using
[studyofhands](https://github.com/willpuckett/studyofhands).

![study of hands](.images/sessile_study.svg)

## 🚀 Firmware

This board is designed for RMK. 😏

### 🦀 RMK

Current RMK build is available in the
[Releases](https://github.com/willpuckett/sessile/releases/latest).

You can build the firmware yourself by cloning this repository and running

```bash
cd rmk && cargo make uf2 --release
```

> **Note:** If you haven't previously used Rust to build software for nRF52840,
> you may need to follow the
> [Setup RMK Environment](https://rmk.rs/docs/user_guide/2-2_local_compilation.html#setup-rmk-environment)
> instructions.

### ⚡ ZMK

There is a **no longer maintained** build of ZMK available in the ZMK branch.

> [!CAUTION]
> RMK uses a newer SoftDevice. Once you flash the current version of RMK, you
> won't be able to reflash ZMK without connecting a debug device and doing
> something akin to:

```bash
wget https://nsscprodmedia.blob.core.windows.net/prod/software-and-other-downloads/softdevices/s140/s140_nrf52_7.3.0.zip
wget https://forum.seeedstudio.com/uploads/short-url/eSDX0bezkia89iZ77eduYRwycAt.zip
unzip s140_nrf52_7.3.0.zip 
unzip eSDX0bezkia89iZ77eduYRwycAt.zip
probe-rs erase --chip nrf52840_xxAA # erasexiao
probe-rs download --verify --binary-format hex --chip nRF52840_xxAA s140_nrf52_7.3.0_softdevice.hex # flashsoftdevice
sudo openocd -f interface/cmsis-dap.cfg -f target/nrf52.cfg -c init -c \"reset init\" -c halt -c \"nrf5 mass_erase\" -c \"program Seeed_XIAO_nRF52840_Sense_bootloader-0.6.1_s140_7.3.0.hex verify\" -c reset -c exit # flashbootloader
```

> [!IMPORTANT]
> If you are still using
> [sessile-template](https://github.com/willpuckett/sessile-template/) to build
> zmk, you need to change
> [west.yml](https://github.com/willpuckett/sessile-template/blob/main/config/west.yml)
> to point to zmk branch of this repo.

```diff
manifest:
  remotes:
    - name: zmkfirmware
      url-base: https://github.com/zmkfirmware
    # Additional modules containing boards/shields/custom code can be listed here as well
    # See https://docs.zephyrproject.org/3.2.0/develop/west/manifest.html#projects
    - name: willpuckett
      url-base: https://github.com/willpuckett
  projects:
    - name: zmk
      remote: zmkfirmware
      revision: main
      import: app/west.yml
    - name: sessile
      remote: willpuckett
-     revision: main
+     revision: zmk 
      import: config/west.yml
  self:
    path: config
```

## 🗺️ Keymap

Thanks to the miraculous [caksoylar](https://github.com/caksoylar) for
[keymap-drawer](https://github.com/caksoylar/keymap-drawer/tree/main) which
generates this map.

![Caster Befuddle Variant](.images/keymap.svg)

## 🔌 Matrix Diagram

Sessile uses the following pinout for its matrix:

![sessile_matrix](.images/matrix.svg)

> **Technical Note:** Referencing
> [this pinout sheet provided by Seeed](https://files.seeedstudio.com/wiki/XIAO-BLE/XIAO-nRF52840-pinout_sheet.xlsx),
> the only two exposed high speed pins P0_04/SDA/D4 & P0_05/SCL/D5 have been
> left available for possible encoders in a subsequent revision.

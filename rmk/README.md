# RMK

RMK is a newer arrival to the firmware front, and isn't quite as fully featured.
That said, it's more inline with the firmware I always hoped to find... And
growing every day!

There are a number of useful commands documented in `../package.json`, including
build and probe-rs commands.

## Updating Your Soft Device

To use RMK, you should be on Soft device S140 7.3.0. Begin by installing
probe-rs using scripts (make sure you already have rustup installed
https://rustup.rs)

- ### Linux, macOS
      curl --proto '=https' --tlsv1.2 -LsSf https://github.com/probe-rs/probe-rs/releases/latest/download/probe-rs-tools-installer.sh | sh
- ### Windows
      irm https://github.com/probe-rs/probe-rs/releases/latest/download/probe-rs-tools-installer.ps1 | iex

Running
`npm run erasexiao && npm run flashsoftdevice && npm run flashbootloader` from
project root with your Xiao connected to a debugger should do the trick. You can
check your current soft device by entering the bootloader and reading the last
line of `INFO_UF2.TXT`--if you are already on 7.3.0 no need to update.

## Building

There is a recent build of rmk in this directory under `sessile.uf2`.

If you wish to build RMK yourself,

1. Install rust https://rustup.rs.
2. `rustup target add thumbv7em-none-eabihf`
3. `cargo install rmkit flip-link cargo-make`
4. From the project root, `npm run buildrmk` or `npm run buildrmkclean` to build
   and generate a UF2, or from the rmk directory, run
   `cargo make uf2 --release`.
5. Double tap the button on your Xiao to enter the bootloader and drag the UF2
   to the disk.

## Caveats

The keymap is not fully implemented in RMK. Combos can be setup in
[Vial](https://get.vial.today) once the board has been flashed.

### Tips for nRF52840

Most nice!nano compatible boards have bootloader with SoftDevice pre-flashed.
Since v0.7.x, RMK will remove old SoftDevice Bluetooth stack and replace it with
its own. So if you want to rollback to v0.6.x, or switch to firmwares that use
SoftDevice stack(for example, zmk), you will need to
[re-flash the bootloader](https://nicekeyboards.com/docs/nice-nano/troubleshooting#my-nicenano-seems-to-be-acting-up-and-i-want-to-re-flash-the-bootloader).

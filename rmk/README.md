# RMK

## Building

Automated builds of rmk are in [releases](https://github.com/willpuckett/sessile/releases/latest).

Once flashed, they can be configured via [Vial]()

If you wish to build RMK yourself,

1. Install rust https://rustup.rs.
2. `rustup target add thumbv7em-none-eabihf`
3. `cargo install rmkit flip-link cargo-make`
4. `cd rmk && cargo make uf2 --release`.
5. Double tap the button on your Xiao to enter the bootloader and drag the UF2
   to the disk.

## Tips for nRF52840

Most nice!nano compatible boards have bootloader with SoftDevice pre-flashed.
Since v0.7.x, RMK will remove old SoftDevice Bluetooth stack and replace it with
its own. So if you want to rollback to v0.6.x, or switch to firmwares that use
SoftDevice stack(for example, zmk), you will need to [re-flash the bootloader](https://github.com/willpuckett/sessile?tab=readme-ov-file#zmk).

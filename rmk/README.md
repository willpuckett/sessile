# 🦀 RMK Firmware

## 🚀 Building

Automated builds of RMK are available in [releases](https://github.com/willpuckett/sessile/releases/latest).

Once flashed, they can be configured via [Vial](https://get.vial.today).

### 🛠️ Build It Yourself

If you wish to build RMK yourself:

1. 📦 Install Rust: https://rustup.rs
2. 🎯 Add the target: `rustup target add thumbv7em-none-eabihf`
3. 🔧 Install tools: `cargo install flip-link cargo-make`
4. 🏗️ Build: `cd rmk && cargo make uf2 --release`
5. 📤 Flash: Double tap the button on your XIAO to enter the bootloader and drag the `.uf2` file to the mounted disk

## 💡 Tips for nRF52840

Most nice!nano compatible boards have a bootloader with SoftDevice pre-flashed.

> [!CAUTION]
> Since v0.7.x, RMK removes the old SoftDevice Bluetooth stack and replaces it with its own. 
> 
> If you want to rollback to v0.6.x, or switch to firmwares that use the SoftDevice stack (for example, ZMK), you will need to [re-flash the bootloader](https://github.com/willpuckett/sessile?tab=readme-ov-file#zmk).


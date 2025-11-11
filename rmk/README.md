# 🦀 RMK Firmware

[![Latest Release](https://img.shields.io/github/v/release/willpuckett/sessile?style=for-the-badge&logo=github&label=Latest%20Release&color=green)](https://github.com/willpuckett/sessile/releases/latest)
[![Build Status](https://img.shields.io/github/actions/workflow/status/willpuckett/sessile/rmk.yml?style=for-the-badge&logo=rust&label=Build&color=orange)](https://github.com/willpuckett/sessile/actions/workflows/rmk.yml)
[![Rust](https://img.shields.io/badge/rust-stable-red?style=for-the-badge&logo=rust)](https://www.rust-lang.org/)
[![Target](https://img.shields.io/badge/target-thumbv7em--none--eabihf-blue?style=for-the-badge&logo=arm)](https://doc.rust-lang.org/rustc/platform-support/thumbv7em-none-eabi.html)

## 🚀 Building

Automated builds of RMK are available in
[releases](https://github.com/willpuckett/sessile/releases/latest).

Once flashed, they can be configured via [Vial](https://get.vial.today).

### 🛠️ Build It Yourself

If you wish to build RMK yourself:

1. 📦 Install Rust: https://rustup.rs
2. 🎯 Add the target: `rustup target add thumbv7em-none-eabihf`
3. 🔧 Install tools: `cargo install flip-link cargo-make`
4. 🏗️ Build: `cd rmk && cargo make uf2 --release`
5. 📤 Flash: Double tap the button on your XIAO to enter the bootloader and drag
   the `.uf2` file to the mounted disk

## 💡 Tips for nRF52840

Most nice!nano compatible boards have a bootloader with SoftDevice pre-flashed.

> [!CAUTION]
> Since v0.7.x, RMK removes the old SoftDevice Bluetooth stack and replaces it
> with its own.
>
> If you want to rollback to v0.6.x, or switch to firmwares that use the
> SoftDevice stack (for example, ZMK), you will need to
> [re-flash the bootloader](https://github.com/willpuckett/sessile?tab=readme-ov-file#zmk).

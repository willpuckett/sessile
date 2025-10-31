# ⚡ ZMK

This is a **no longer maintained** build of ZMK.

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
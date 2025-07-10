# ZMK

ZMK probably is still somewhat more fully featured and stable, but this board
was intended to have a rust based firmware.

RMK has improved substantially enough that it is now provided as the default
firmware for this board.

If you are still using the [sessile-template](https://github.com/willpuckett/sessile-template/) to build zmk, you need to change [west.yml](https://github.com/willpuckett/sessile-template/blob/main/config/west.yml) to point to the zmk branch of this repo.

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
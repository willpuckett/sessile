# Sessile

![sessile render](.images/render.webp)

*Sessile* is a further exploration of "minimal" finger travel.

## What Even Is 'Minimal Finger Travel' Anyway?

Probably the least amount of finger travel would be not moving them at all. That would be 10 keys...

```math
combos_{10\,keys} = \sum_{r=1}^{10} C(10, r) = 1023
```

...yielding 1023 possible combinations. 

More realstically, we might consider excluding cross hand combinations so that modifiers might be used. That would give us 

```math
combos_{5\,keys} = \sum_{r=1}^{5} C(5, r) = 31
```

So, with only 5 keys on both hands, and no cross hand combos, we would have a total of 62 possible keys per layer—more than sufficient.

I wasn't quite ready to take on learning to type on that though, so just avoiding lateral reaches seemed like a start. 🙃

*Sessile* was produced using [studyofhands](https://github.com/willpuckett/studyofhands). 

## Features

- Sessile uses KLP-Lame keycaps. Larger caps may be tight, especially on the bottom row. I was lazy and didn't model the tilted keycaps in the rendering, but they're much nicer for the vertical combos.

- Uses battery LIR1254.

- The high speed pins were left available for encoders and *could* be wired in a subesquent revision.

- Built with RMK. Combos soon to follow upon upstream merge.

